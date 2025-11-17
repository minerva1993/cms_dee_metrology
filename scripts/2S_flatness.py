import pylab as py, pandas as pd


hist_bin_size=0.01

Dee_name = 'DD12-E-001'


data_top  = pd.read_csv('../'+Dee_name+'/results/'+'2S_flatness_top.csv', skiprows=5, encoding='latin')
data_bottom = pd.read_csv('../'+Dee_name+'/results/'+'2S_flatness_bottom.csv', skiprows=5, encoding='latin')

max_top = data_top.Meas.max()
max_bot = data_bottom.Meas.max()

fig = py.figure(figsize=[9,4])
ax = fig.add_subplot(121)
py.hist(data_top.Meas, bins = py.arange(0,max_top+hist_bin_size,hist_bin_size))
py.title('2S contact flatness top')
py.xlabel('flatness [mm]')
py.ylabel('# positions')
ax = fig.add_subplot(122)
py.hist(data_bottom.Meas, bins = py.arange(0,max_bot+hist_bin_size,hist_bin_size))
py.title('2S contact flatness bottom')
py.xlabel('flatness [mm]')
py.ylabel('# positions')



py.show()

sfijefisjdfo
X_data = data_raw[data_raw.Control=='X'].set_index('Name')
Y_data = data_raw[data_raw.Control=='Y'].set_index('Name')
Z_data = data_raw[data_raw.Control=='Z'].set_index('Name')

# out of spec
oos1 = (X_data.Dev**2 + Y_data.Dev**2)**0.5 > 0.1
oos2 = (X_data.Dev**2 + Y_data.Dev**2)**0.5 > 0.2


fig = py.figure()
ax = fig.add_subplot(111)
py.quiver(X_data.Nom,Y_data.Nom,X_data.Dev,Y_data.Dev,color='g',scale=1.0/500,scale_units='xy',label='<100 um')
py.quiver(X_data.Nom[oos1],Y_data.Nom[oos1],X_data.Dev[oos1],Y_data.Dev[oos1],color='y',scale=1.0/500,scale_units='xy',label='>100um & <200 um')
py.quiver(X_data.Nom[oos2],Y_data.Nom[oos2],X_data.Dev[oos2],Y_data.Dev[oos2],color='r',scale=1.0/500,scale_units='xy',label='>200 um')
#py.quiver(300,600,0.3,0,scale=1.0/500,scale_units='xy')
#py.text(300,630,'300um, scale 500:1')
py.xlabel('mm')
py.ylabel('mm')
py.legend()
py.title(Dee_name+', PS inserts, Top side')
py.xlim([-750,750])
py.ylim([-50,750])
ax.set_aspect(1)
ax.invert_xaxis()
ax.invert_yaxis()



data_raw  = pd.read_csv('PSinserts_bottom.csv', skiprows=5, encoding='latin')

X_data = data_raw[data_raw.Control=='X'].set_index('Name')
Y_data = data_raw[data_raw.Control=='Y'].set_index('Name')
Z_data = data_raw[data_raw.Control=='Z'].set_index('Name')

# out of spec
oos1 = (X_data.Dev**2 + Y_data.Dev**2)**0.5 > 0.1
oos2 = (X_data.Dev**2 + Y_data.Dev**2)**0.5 > 0.2


fig = py.figure()
ax = fig.add_subplot(111)
py.quiver(X_data.Nom,Y_data.Nom,X_data.Dev,Y_data.Dev,color='g',scale=1.0/500,scale_units='xy',label='<100 um')
py.quiver(X_data.Nom[oos1],Y_data.Nom[oos1],X_data.Dev[oos1],Y_data.Dev[oos1],color='y',scale=1.0/500,scale_units='xy',label='>100um & <200 um')
py.quiver(X_data.Nom[oos2],Y_data.Nom[oos2],X_data.Dev[oos2],Y_data.Dev[oos2],color='r',scale=1.0/500,scale_units='xy',label='>200 um')
#py.quiver(300,600,0.3,0,scale=1.0/500,scale_units='xy')
#py.text(300,630,'300um, scale 500:1')
py.xlabel('mm')
py.ylabel('mm')
py.legend()
py.title(Dee_name+', PS inserts, Bottom side')
py.xlim([-750,750])
py.ylim([-50,750])
ax.set_aspect(1)
ax.invert_yaxis()


py.show()
