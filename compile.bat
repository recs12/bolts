:: app name: bolts
:: Set this file for compiling the executable of the macro.
:: So it can be added to the user custom theme in solidedge. 
ipyc.exe /main:./bolts/__main__.py ^
./bolts/Interop.SolidEdge.dll ^
./bolts/api.py ./bullet/holes.py ^
./bolts/equivalences.py ^
./bolts/customs.py ^
/embed ^
/out:bolts_macro_64x_0-0-0 ^
/platform:x64 ^
/standalone ^
/target:exe ^
/win32icon:logo.ico 
