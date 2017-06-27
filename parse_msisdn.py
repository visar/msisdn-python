class ParseMSISDN(object):
    @classmethod
    def transform(cls, msisdn):
        if not msisdn.isdigit():
            raise ValueError("Input parameter must be integer")
        if len(msisdn) > 15:
            raise ValueError("Input should be 15 digits at most")
        result = dict(mno_identifier=0,
                      country_dialing_code=0,
                      subscriber_number=0,
                      country_identifier=0,)
        return result
