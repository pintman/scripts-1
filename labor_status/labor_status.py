import urllib.request

URL = "https://das-labor.org/status/status.php?status"


def get_labor_status():
    """
    Ermittelt den Status des Bochumer Labors: OPEN oder CLOSED.

    >>> get_labor_status() in ['CLOSED' , 'OPEN']
    True
    """
    response = urllib.request.urlopen(URL)
    status = str(response.readline(), encoding='UTF-8')
    return status


if __name__ == '__main__':
    print(get_labor_status())
