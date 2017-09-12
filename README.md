## Ettus X300 experiments
1) The Python scripts attached on this project will help you generate, store and parse IQ data from Ettus boards (like the X-series, N-series, etc).

2) The dependencies required are listed here: https://gnuradio.org/doc/doxygen/build_guide.html

3) Example: To obtain IQ data (200 MSps centered at 700 MHz for 15 seconds with 5 dB Rx gain), run the following script:
```
python run_python.py -f 700e6 -g 5 -t 15 -s 200e6
```

4) To parse the above IQ data and view resulting power vs time vs frequency plot, run:
```
python parse_fft.py --filename <generated file>
```

5) Appended metadata, example fields:
```
cat <generated file>.json
 > {"device": "USRPX310", "data type": "sc16 interleaved", "center frequency (MHz)": 700.0, "name": "University of Washington - Sieg Hall", "antenna": "Multipolarized Super-M Ultra Base Station (25MHz-6GHz)", "antenna height (above ground level) in Feet": 50, "number of samples": 3000000000, "sampling rate (MSps)": 200.0, "longitude": -122.306728, "gain (dB)": 0.0, "time": "2017_09_11-17_57_00", "latitude": 47.654839}
```

6) Attached is an IQ data file generated from roof-top setting (UW01), for 200 MSps centered at 700 MHz for 15 seconds with 5 dB Rx gain: https://drive.google.com/drive/folders/0B4xmUvk8OazBVHpIcEVVUTNSbEk?usp=sharing
