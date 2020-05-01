:: app name: bolts
:: Set this file for compiling the executable of the macro.
:: So it can be added to the user custom theme in solidedge. 
ipyc.exe /main:./bolts/__main__.py ./bolts/api.py ./bolts/convertion.py ^
./bolts/Interop.SolidEdge.dll ^
/embed ^
/out:bolts_macro_recs_64x_0-0-4 ^
/platform:x64 ^
/standalone ^
/target:exe ^
/win32icon:bolt.ico 
