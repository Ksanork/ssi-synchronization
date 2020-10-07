# ssi-synchronization

Repozytorium zawiera dodatkowe moduły pomocne przy synchronizacji strumieni danych za pomocą frameworka SSI (https://github.com/hcmlab/ssi)

### Sensory:
#### simple_columns_csv_sensor

Pozwala na stworzenie strumienia liczb zmiennoprzecinkowych z daną częstotliwością z pliku `csv`
Dotyczy jedynie plików, które składają się z jednej kolumny danych.

Domyślny format zakłada, że pierwsza linia w pliku `csv` to data (_timestamp_) a druga to częstotliwość

Plik `01_sensor.pipeline` pokazuje przykładowe wykorzystanie w pipeline.
##### Przykład użycia:
```xml
<sensor create="PythonSensor" optsstr="path=HR.csv;headers_ln=2;sr=10.0" script="simple_columns_csv_sensor" block="0.1">
    <output channel="csv_data" pin="hr" />
</sensor>
```

##### Parametry:
* `path` - scieżka do pliku `csv`, typ `STRING`
* `sr` - częstotliwość (_sample rate_), typ `FLOAT`, jeżeli również `auto_init` ustawione jest jako `1` to brany pod uwagę jest paramatr `sr`, a nie wartość z pliku
* `headers_ln` - ilość lini nagłówkowych na początku pliku, którę będą ignorowane podczas wczytywania danych do strumienia, typ `INTEGER`
* `auto_init` - jeżeli ustawione jako `1` to skrypt stara się pobrać częstotliwość z linii nagłówkowych (na podstawie domyślnego formatu opisanego wyżej). Domyślnie ustawione jako `1`

##### Przykładowy plik csv:
```csv
1600692252.000000
100.000
1.0
2.0
3.0
4.0
...
```