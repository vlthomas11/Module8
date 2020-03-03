from datetime import datetime, timedelta


def half_birthday(dob):
    dob_date = datetime.strptime(dob, '%m/%d/%Y')
    half_dob = dob_date + timedelta(days=183)
    return half_dob


if __name__ == '__main__':
    half_birthday('12/01/2019')