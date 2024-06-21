import locale


def rupiah_formatting(amount, with_prefix=True, decimal=0):
    locale.setlocale(locale.LC_NUMERIC, 'id_ID.utf8')
    result = locale.format_string("%.*f", (decimal, amount), True)
    if with_prefix:
        return "Rp. {}".format(result)
    return result

def convert_rupiah_to_float(amount_with_currency):
    locale.setlocale(locale.LC_NUMERIC, 'id_ID.utf8') #sudo apt-get install language-pack-id
    amount = locale.atof(amount_with_currency.strip("Rp. "))

    return float(amount)