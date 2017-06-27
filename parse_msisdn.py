from difflib import Differ


class ParseMSISDN(object):
    @classmethod
    def transform(cls, msisdn):
        if msisdn[0] == '+':
            msisdn = msisdn[1:]
        if not msisdn.isdigit():
            raise ValueError("Input parameter must be integer")
        if len(msisdn) > 15:
            raise ValueError("Input should be 15 digits at most")

        country_codes = dict()
        mno_providers = dict()

        with open('country_codes', 'r') as f:
            for line in f:
                (key, val) = line.split(' ', 1)
                country_codes[key.strip()] = val.strip()

        with open('mno_providers', 'r') as f:
            for line in f:
                (key, val) = line.split(' ', 1)
                mno_providers[key.strip()] = val.strip()

        for length in range(1, 5):
            if msisdn[0: length] in country_codes:
                country_identifier = country_codes[msisdn[0: length]]
                country_dialing_code = msisdn[0: length]
                for operator_length in range(1, 5):
                    if msisdn[0: length + operator_length] in mno_providers:
                        mno_identifier = mno_providers[
                            msisdn[0: length + operator_length]]
                        diff = "".join(item[2:] for item in
                                       Differ().compare(
                                           list(country_dialing_code),
                                           msisdn[0: length + operator_length])
                                       if item[0] == '+')
                        subscriber_number = diff + msisdn[length + operator_length:]

        if mno_identifier is None or subscriber_number is None:
            raise Exception("Invalid number")

        return dict(mno_identifier=mno_identifier,
                    country_dialing_code=country_dialing_code,
                    subscriber_number=subscriber_number,
                    country_identifier=country_identifier, )
