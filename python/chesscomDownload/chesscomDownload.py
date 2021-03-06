from requests import get

baseYear = 2017
for iYear in range(5):
    for iMonth in range(12):
        rYear = str(baseYear + iYear)
        rMonth = str(iMonth + 1)
        if (len(rMonth) == 1):
            rMonth = '0' + rMonth
        rPeriod = rYear + '/' + rMonth
        print('Downloading: ' + rPeriod)
        startUrl = 'https://api.chess.com/pub/player/mrkaranj/games/'
        endUrl = '/pgn'
        url = startUrl + rPeriod + endUrl
        response = get(url)
        fileName = rYear + '_' + rMonth + '.txt'
        if (len(response.text) != 0):
            print('Saving to: ' + fileName)
            with open(fileName , 'a') as output:
                output.write(response.text)
        else:
            print('No games found')