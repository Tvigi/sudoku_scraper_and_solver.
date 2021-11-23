from urllib import request
from bs4 import BeautifulSoup as bs

def scrape():
    sudoku_url = 'http://nine.websudoku.com/'

    #Otvaranje stranice povezivanje i zatvaranje stranice
    client = request.urlopen(sudoku_url)
    page_html = client.read()
    client.close()

    #html parsiranje
    page_soup = bs(page_html, 'html.parser')

    #nalazi div u kojem se nalazi tabela
    sudoku_grid = page_soup.find(id='puzzle_container')

    #nalazenje svih redova u tabeli
    sudoku_grid_rows = sudoku_grid.find_all('tr')

    #rezultirajuca matrica sudokua za pocetak je samo popunjena nulama 
    #u polja koja nisu prazna cemo upisati vrijednost
    result_grid = [[0]*9 for i in range(9)]

    for (row_index, row) in enumerate(sudoku_grid_rows):

        #nalazenje svih polja(cells) u jednom redu tabele
        row = row.find_all('td')

        for (cell_index, cell) in enumerate(row):

            #sama vrijednost se nalazi u input tagu pa treba njega naci
            cell = cell.find('input')

            #konverzija u string a bi nasli value 
            cell = str(cell)

            value_index = cell.find('value')
            value_index = int(value_index)

            if value_index != -1:
                cell_value = cell[value_index+7: value_index+8]
                result_grid[row_index][cell_index] = int(cell_value)
    
    return result_grid

scrape()