def calculate_score(sesso, eta, bmi, attivita, ore_sport, obiettivo):
  if sesso == 'uomo':
    punteggio = 50
  elif sesso == 'donna':
    punteggio = 46
  
  if eta == '0-20':
    pass
  elif eta == '21-35':
    punteggio = punteggio - 2
  elif eta == '36-50':
    punteggio = punteggio - 4
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
  elif bmi == '40+':
    punteggio = punteggio - 10
  
  if attivita == 'leggera':
    pass
  if attivita == 'media':
    punteggio = punteggio + 2
  if attivita == 'pesante':
    punteggio = punteggio + 4
  
  if ore_sport == '0':
    pass
  if ore_sport == '1-3':
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

  return punteggio