#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"Making year dependent driver colour"


#2018
DRIVER_COLORS_2018 = {'HAM': '#00d2be', 'BOT': '#1affe8', 'VER': '#0600ef', 'RIC': '#0800b5', 
                      'ALO': '#ff8700', 'VAN': '#ff6700', 'RAI': '#dc0000', 'VET': '#ff1a1a',
                      'SAI': '#FFF500', 'HUL': '#fffa66', 'PER': '#f596c8', 'OCO': '#f8b9db', 
                      'GAS': '#469bff', 'HAR': '#d9d9d9', 'LEC': '#900000', 'ERI': '#660000', 
                      'STR': '#f2f2f2', 'SIR': '#ffffff', 'GRO': '#F0D787', 'MAG': '#e9c349',
                      'KVY': '#469bff'}

#2019
DRIVER_COLORS_2019 = {'HAM': '#00d2be', 'BOT': '#1affe8', 'VER': '#0600ef', 'ALB': '#0800b5', 
                      'NOR': '#ff8700', 'SAI': '#ff6700', 'LEC': '#dc0000', 'VET': '#ff1a1a',
                      'RIC': '#FFF500', 'HUL': '#fffa66', 'PER': '#f596c8', 'STR': '#f8b9db', 
                      'GAS': '#469bff', 'KVY': '#d9d9d9', 'RAI': '#900000', 'GIO': '#660000', 
                      'RUS': '#f2f2f2', 'KUB': '#ffffff', 'GRO': '#F0D787', 'MAG': '#e9c349'}

#2020
DRIVER_COLORS_2020 = {'HAM': '#00d2be', 'BOT': '#1affe8', 'VER': '#0600ef', 'ALB': '#0800b5', 
                      'NOR': '#ff8700', 'SAI': '#ff6700', 'LEC': '#dc0000', 'VET': '#ff1a1a',
                      'RIC': '#FFF500', 'OCO': '#fffa66', 'PER': '#f596c8', 'STR': '#f8b9db', 
                      'GAS': '#c8c8c8', 'KVY': '#1a85ff', 'RAI': '#900000', 'GIO': '#660000', 
                      'RUS': '#0082fa', 'LAT': '#1a7cff', 'GRO': '#787878', 'MAG': '#595959',
                      'HUL': '#f596c8', 'FIT': '#787878', 'AIT': '#0082fa'}
    
#2021
DRIVER_COLORS_2021 = {'HAM': '#00d2be', 'BOT': '#1affe8', 'VER': '#0600ef', 'PER': '#0800b5', 
                      'NOR': '#ff8700', 'RIC': '#ff6700', 'LEC': '#dc0000', 'SAI': '#ff1a1a',
                      'ALO': '#0090ff',  'OCO': '#66bdff', 'VET': '#006f62', 'STR': '#004225', 
                      'GAS': '#2b4562', 'TSU': '#4670a0', 'RAI': '#900000', 'GIO': '#660000', 
                      'RUS': '#005aff', 'LAT': '#1a7cff', 'MSC': '#ffffff', 'MAZ': '#FAF9F6',
                      'KUB': '#900000'}

#2022
DRIVER_COLORS_2022 = {'HAM': '#00d2be', 'RUS': '#1affe8', 'VER': '#0600ef', 'PER': '#0800b5', 
                      'NOR': '#ff8700', 'RIC': '#ff6700', 'LEC': '#dc0000', 'SAI': '#ff1a1a',
                      'ALO': '#0090ff',  'OCO': '#66bdff', 'VET': '#006f62', 'STR': '#004225', 
                      'GAS': '#2b4562', 'TSU': '#4670a0', 'BOT': '#900000', 'ZHO': '#660000', 
                      'ALB': '#005aff', 'LAT': '#1a7cff', 'MSC': '#ffffff', 'MAG': '#FAF9F6'}


def driver_year_color(identifier, year):
   if year == 2018:
       return DRIVER_COLORS_2018[identifier] 
   if year == 2019:
       return DRIVER_COLORS_2019[identifier] 
   if year == 2020:
        return DRIVER_COLORS_2020[identifier]
   if year == 2021:
        return DRIVER_COLORS_2021[identifier]
   if year == 2022:
       return DRIVER_COLORS_2022[identifier]
   else:
       return None
            
     




