
from tqdm import tqdm

import pandas as pd
import itertools

# Definire le categorie per ciascuna colonna
sesso = ['uomo', 'donna']
eta = ['0-20', '21-35', '36-50', '51+']
bmi = ['<18', '18-25', '25-30', '30-35', '35-40', '40+']
attivita = ['leggera', 'media', 'pesante']
ore_sport = ['0', '1-3', '4-6', '7+']
obiettivo = ['mantenimento', 'dimagrimento', 'aumento']

# Generare tutte le combinazioni possibili
combinations = list(itertools.product(sesso, eta, bmi, attivita, ore_sport, obiettivo))

# Creare un DataFrame con le combinazioni
df = pd.DataFrame(combinations, columns=['sesso', 'eta', 'bmi', 'attivita', 'ore sport', 'obiettivo'])

df['puntegigo']

breakpoint()

def calculate_score(sesso, eta, bmi, attivita, ore_sport, obiettivo)
  if sesso == 'uomo':
    punteggio = 50
  elif sesso == 'donna':
    punteggio = 46

  if eta == '0-20':
    pass
  elif eta == '21-35':
    punteggio = punteggio - 2
  elif eta == '36-50':
    puntegigo = punteggio - 4
  elif eta == '51+':
    punteggio = punteggio - 6

  if bmi == '<18':
    pass
  elif bmi == '18-25':
    punteggio = punteggio - 2
  elif bmi == '25-30':
    punteggio = punteggio - 4
  elif bmi == '30-35':
    punteggio = punteggio - 6
  elif bmi == '35-40':
    punteggio = punteggio - 8

  if attivita == 'leggera':
    pass
  if attivita == 'media':
    punteggio = punteggio + 2
  if attivita == 'pesante':
    punteggio = punteggio + 4

  if ore_sport == '0':
    pass
  if rore_sport == '1-3':
    punteggio = punteggio + 2
  if ore_sport == '4-6':
    punteggio = punteggio + 4
  if ore_sport == '7+':
    punteggio = punteggio + 6

  if obiettivo == 'mantenimento':
    pass
  if obiettivo == 'dimagrimento':
    punteggio = punteggio - 4
  if obiettivo == 'aumento':
    punteggio = punteggio + 4