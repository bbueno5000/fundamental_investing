
import time
import urllib

sp500short = [
    'a', 
    'aa', 
    'aapl', 
    'abbv', 
    'abc', 
    'abt', 
    'ace', 
    'aci', 
    'acn', 
    'act', 
    'adbe', 
    'adi', 
    'adm', 
    'adp',
    'rsh'
    ]

def key_statistics(stock):
    """
    Definitions:
        pbr - price to book ratio
        pe12t - trailing price/earnings (12 months)
        peg5 - price/earnings to growth ratio (5 years expected)
    """
    try:
        source_code = urllib.urlopen('http://finance.yahoo.com' + stock).read()
        pbr = source_code.split('Price/Book')[1].split('</td>')[0]
        if float(pbr) < 0.70:
            print('Price/Book:', stock, pbr)
            peg5 = source_code.split(
                'PEG Ratio (5 yr expected)<font size="-1"><sup>1</sup></font>:</td><td class="yfnc_tabledata1">'
                )[1].split('</td>')[0]
            if 0 < float(peg5) < 1:
                pe12t = sourceCode.split(
                    'Trailing P/E (ttm, intraday):</td><td class="yfnc_tabledata1">'
                    )[1].split('</td>')[0]
                print(stock, 'meets requirements')
                print('Price to book ratio:', pbr)
                print('PEG forward 5 years', peg5)
                print('Trailing P/E (12mo):', pe12t)
    except Exception as e:
        print('error:main loop:', str(e))

if __name__ == '__main__':
    for stock in sp500short:
        key_statistics(stock)
        time.sleep(1)
