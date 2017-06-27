import unittest
from parse_msisdn import ParseMSISDN


class TestParseMSISDN(unittest.TestCase):
    def test_result_is_dict(self):
        msisdn = "38976123456"
        result = ParseMSISDN.transform(msisdn)
        self.assertIsInstance(result, dict)

    def test_leading_plus(self):
        msisdn = "+38976123456"
        result = ParseMSISDN.transform(msisdn)
        self.assertIsInstance(result, dict)

    def test_check_keys(self):
        msisdn = "38976123456"
        result = ParseMSISDN.transform(msisdn)
        self.assertIn('mno_identifier', result.keys())
        self.assertIn('country_dialing_code', result.keys())
        self.assertIn('subscriber_number', result.keys())
        self.assertIn('country_identifier', result.keys())

    def test_input_is_digits_only(self):
        msisdn = "123456789a"
        self.assertRaises(ValueError, ParseMSISDN.transform, msisdn)

    def test_input_is_correct_length(self):
        msisdn = "1234567890123456"
        self.assertRaises(ValueError, ParseMSISDN.transform, msisdn)

    def test_country_dialing_code(self):
        msisdn = "38976123456"
        result = ParseMSISDN.transform(msisdn)
        self.assertEqual(result['country_dialing_code'], "389")

    def test_country_dialing_code_with_leading_plus(self):
        msisdn = "+38976123456"
        result = ParseMSISDN.transform(msisdn)
        self.assertEqual(result['country_dialing_code'], "389")

    def test_country_identifier(self):
        msisdn = "38976123456"
        result = ParseMSISDN.transform(msisdn)
        self.assertEqual(result['country_identifier'], "MK")

    def test_country_identifier_with_leading_plus(self):
        msisdn = "+38976123456"
        result = ParseMSISDN.transform(msisdn)
        self.assertEqual(result['country_identifier'], "MK")

    def test_mno_identifier(self):
        msisdn = "38976123456"
        result = ParseMSISDN.transform(msisdn)
        self.assertEqual(result['mno_identifier'], "VIP Operator")

    def test_mno_identifier_with_leading_plus(self):
        msisdn = "+38976123456"
        result = ParseMSISDN.transform(msisdn)
        self.assertEqual(result['mno_identifier'], "VIP Operator")

    def test_subscriber_number(self):
        msisdn = "38976123456"
        result = ParseMSISDN.transform(msisdn)
        self.assertEqual(result['subscriber_number'], "123456")

    def test_subscriber_number_with_leading_plus(self):
        msisdn = "+38976123456"
        result = ParseMSISDN.transform(msisdn)
        self.assertEqual(result['subscriber_number'], "123456")

    def test_nonexisting_number(self):
        msisdn = "99999999999"
        self.assertRaises(Exception, ParseMSISDN.transform, msisdn)

    def test_nonexisting_number_with_leading_plus(self):
        msisdn = "+99999999999"
        self.assertRaises(Exception, ParseMSISDN.transform, msisdn)

    def test_slovenian_number(self):
        msisdn = "+38640658494"
        result = ParseMSISDN.transform(msisdn)
        self.assertEqual(result['country_identifier'], "SI")
        self.assertEqual(result['country_dialing_code'], "386")
        self.assertEqual(result['mno_identifier'], "Si.mobil")
        self.assertEqual(result['subscriber_number'], "658494")

if __name__ == '__main__':
    unittest.main()
