"""Convierte un Excel compatible a datos.js junto a este script."""
import sys
from pathlib import Path
import pandas as pd

if len(sys.argv) != 2:
    raise SystemExit('Uso: python convertir_datos.py archivo.xlsx')
df = pd.read_excel(sys.argv[1], sheet_name='Sheet1')
cols = ['id', 'edad', 'nivel_edu', 'ingreso_mensual', 'sex', 'anios_esc']
if not set(cols).issubset(df.columns):
    raise SystemExit('Faltan columnas: ' + ', '.join(set(cols)-set(df.columns)))
df = df[cols].copy()
if df.empty or df.isna().any().any():
    raise SystemExit('El archivo está vacío o contiene valores faltantes; revise antes de convertir.')
for col in ['id', 'edad', 'ingreso_mensual', 'anios_esc']:
    df[col] = pd.to_numeric(df[col], errors='raise')
    if not df[col].map(lambda v: float('-inf') < v < float('inf')).all():
        raise SystemExit('Valor no finito en ' + col)
df['nivel_edu'] = df['nivel_edu'].astype(str).str.strip().replace({'Prrimaria completa': 'Primaria completa'})
df['sex'] = df['sex'].astype(str).str.strip()
Path(__file__).with_name('datos.js').write_text('window.DATA = ' + df.to_json(orient='records', force_ascii=False) + ';\n', encoding='utf-8')
print(f'Convertidos {len(df):,} registros. Revise límites de edad y metadatos de la interfaz si cambió de fuente.')
