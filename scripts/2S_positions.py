import pylab as py, pandas as pd
import numpy as np
import os
from matplotlib.patches import Arc, RegularPolygon

#select only one Dee to process
Dee_name = 'DD12-E-001'

files = ['2S_positions_top.csv','2S_positions_bottom.csv']
side = ['Top', 'Bottom']
#files = ['2S_positions_top.csv']
#side = ['Top']

full_disk_dfs = []

def drawCirc(ax,radius,centX,centY,angle_,theta2_,color_='black',lw_=3):
    #========Line
    if theta2_ >0:

        arc = Arc([centX,centY],radius,radius,angle=angle_,
            theta1=0,theta2=theta2_,capstyle='round',linestyle='-',lw=lw_,color=color_)
    else:
        arc = Arc([centX,centY],radius,radius,angle=angle_+theta2_,
            theta1=0,theta2=-theta2_,capstyle='round',linestyle='-',lw=lw_,color=color_)

    ax.add_patch(arc)


    # #========Create the arrow head
    # endX=centX+(radius/2)*py.cos(py.radians(theta2_+angle_)) #Do trig to determine end position
    # endY=centY+(radius/2)*py.sin(py.radians(theta2_+angle_))
    #
    # ax.add_patch(                    #Create triangle as arrow head
    #     RegularPolygon(
    #         (endX, endY),            # (x,y)
    #         3,                       # number of vertices
    #         radius/5,                # radius
    #         py.radians(angle_+theta2_),     # orientation
    #         color=color_
    #     )
    # )



for f,s in zip(files,side):

    data_raw  = pd.read_csv('../'+Dee_name+'/results/'+f, skiprows=5, encoding='latin')

    X_data = data_raw[data_raw.Control=='X'].set_index('Name')
    Y_data = data_raw[data_raw.Control=='Y'].set_index('Name')
    Z_data = data_raw[data_raw.Control=='Z'].set_index('Name')

    # out of spec
    oos1 = (X_data.Dev**2 + Y_data.Dev**2)**0.5 > 0.1
    oos2 = (X_data.Dev**2 + Y_data.Dev**2)**0.5 > 0.3


    fig = py.figure(figsize=[8,4])
    ax = fig.add_subplot(111)
    py.quiver(X_data.Nom,Y_data.Nom,X_data.Dev,Y_data.Dev,color='g',scale=1.0/500,scale_units='xy',label='<100 um')
    py.quiver(X_data.Nom[oos1],Y_data.Nom[oos1],X_data.Dev[oos1],Y_data.Dev[oos1],color='y',scale=1.0/500,scale_units='xy',label='>100um & <300 um')
    py.quiver(X_data.Nom[oos2],Y_data.Nom[oos2],X_data.Dev[oos2],Y_data.Dev[oos2],color='r',scale=1.0/500,scale_units='xy',label='>300 um')
    #py.quiver(300,600,0.3,0,scale=1.0/500,scale_units='xy')
    #py.text(300,630,'300um, scale 500:1')
    py.xlabel('mm')
    py.ylabel('mm')
    py.legend()
    py.title(Dee_name+', 2S Positions, '+s+' side')
    py.xlim([-1100,1100])
    py.ylim([-50,1100])
    ax.set_aspect(1)
    if s=='Top': ax.invert_xaxis()
    ax.invert_yaxis()
    py.savefig('../'+Dee_name+'/plots/2S_inserts_'+s+'.png',dpi=600)
    py.savefig('../'+Dee_name+'/plots/2S_inserts_'+s+'.pdf')

    module = pd.DataFrame(index=range(int(len(X_data)/5)))
    module['X1n'] = pd.array(X_data.Nom[0::5])
    module['Y1n'] = pd.array(Y_data.Nom[0::5])
    module['X2n'] = pd.array(X_data.Nom[1::5])
    module['Y2n'] = pd.array(Y_data.Nom[1::5])
    module['X3n'] = pd.array(X_data.Nom[2::5])
    module['Y3n'] = pd.array(Y_data.Nom[2::5])
    module['X4n'] = pd.array(X_data.Nom[3::5])
    module['Y4n'] = pd.array(Y_data.Nom[3::5])
    module['X5n'] = pd.array(X_data.Nom[4::5])
    module['Y5n'] = pd.array(Y_data.Nom[4::5])
    module['X1m'] = pd.array(X_data.Meas[0::5])
    module['Y1m'] = pd.array(Y_data.Meas[0::5])
    module['X2m'] = pd.array(X_data.Meas[1::5])
    module['Y2m'] = pd.array(Y_data.Meas[1::5])
    module['X3m'] = pd.array(X_data.Meas[2::5])
    module['Y3m'] = pd.array(Y_data.Meas[2::5])
    module['X4m'] = pd.array(X_data.Meas[3::5])
    module['Y4m'] = pd.array(Y_data.Meas[3::5])
    module['X5m'] = pd.array(X_data.Meas[4::5])
    module['Y5m'] = pd.array(Y_data.Meas[4::5])
    module['X1d'] = pd.array(X_data.Dev[0::5])
    module['Y1d'] = pd.array(Y_data.Dev[0::5])
    module['X2d'] = pd.array(X_data.Dev[1::5])
    module['Y2d'] = pd.array(Y_data.Dev[1::5])
    module['X3d'] = pd.array(X_data.Dev[2::5])
    module['Y3d'] = pd.array(Y_data.Dev[2::5])
    module['X4d'] = pd.array(X_data.Dev[3::5])
    module['Y4d'] = pd.array(Y_data.Dev[3::5])
    module['X5d'] = pd.array(X_data.Dev[4::5])
    module['Y5d'] = pd.array(Y_data.Dev[4::5])
    module['CenterXn'] = module.X3n
    module['CenterYn'] = module.Y3n
    module['CenterXm'] = module.X3m
    module['CenterYm'] = module.Y3m
    module['CenterXd'] = module.X3d
    module['CenterYd'] = module.Y3d

    #print(module)
    columns_to_print = ['CenterXn', 'CenterXm', 'CenterXd', 'CenterYn', 'CenterYm', 'CenterYd']
    print(module[columns_to_print].to_string(index=False))

    # module['angle_dev'] = py.arctan((module.Y2m-module.Y1m)/(module.X2m-module.X1m)) - py.arctan((module.Y2n-module.Y1n)/(module.X2n-module.X1n))
    # module['i1i2_dist_dev'] = ((module.Y2m-module.Y1m)**2+(module.X2m-module.X1m)**2)**0.5 - 125
    # module['i1i3_dist_dev'] = ((module.Y3m-module.Y1m)**2+(module.X3m-module.X1m)**2)**0.5 - 136.67
    # module['i2_nofit'] = abs(module.i1i2_dist_dev)>0.2
    # module['i3_nofit'] = (module.i1i2_dist_dev**2+(py.tan(module.angle_dev) * 136.67)**2)**0.5  > 0.45
    # module['CenterXn'] = (module.X1n+module.X3n)/2
    # module['CenterYn'] = (module.Y1n+module.Y3n)/2
    # module['i1i3_vect_X'] = (module.X3n-module.X1n)/136.67
    # module['i1i3_vect_Y'] = (module.Y3n-module.Y1n)/136.67
    # module['CenterXm'] = module.CenterXn + module.X1d + module.i1i3_vect_Y * py.tan(module.angle_dev)*68.335 # i1-13 vector, swap X and Y for orthogonal direction of rotation
    # module['CenterYm'] = module.CenterYn + module.Y1d + module.i1i3_vect_X * py.tan(module.angle_dev)*68.335 # needs checking if the orientatio is OK
    # module['CenterXd'] = module.CenterXm - module.CenterXn
    # module['CenterYd'] = module.CenterYm - module.CenterYn
    #
    # if sum(module.i2_nofit)>0 or sum(module.i3_nofit)>0 :
    #     print('WARNING: At least one module might not fit to the inserts.')
    #
    # #print(module.iloc[:,18:])
    #
    #
    #

    oos2 = py.hypot(module.CenterXd,module.CenterYd) > 0.3


    fig = py.figure(figsize=[8,4])
    ax = fig.add_subplot(111)
    py.quiver(module.CenterXn,module.CenterYn,module.CenterXd,module.CenterYd,color='g',scale=1.0/500, headwidth=1, headlength=0,scale_units='xy',label='<300 um')
    py.quiver(module.CenterXn[oos2],module.CenterYn[oos2],module.CenterXd[oos2],module.CenterYd[oos2],color='r',scale=1.0/500, headwidth=1, headlength=0,scale_units='xy',label='>300 um')

    angle_devs = []

    for r,m in module.iterrows():
        #nominal vector using 3 and 5
        #should move this out of the loop and make column in module object
        nom_vect_x = m.X5n - m.X3n
        nom_vect_y = m.Y5n - m.Y3n
        nom_angle = py.degrees(py.arctan2(nom_vect_y, nom_vect_x))
        meas_vect_x = m.X5m - m.X3m
        meas_vect_y = m.Y5m - m.Y3m
        meas_angle = py.degrees(py.arctan2(meas_vect_y, meas_vect_x))
        angle_dev = (meas_angle - nom_angle)

        angle_devs.append(angle_dev)

        if s=='Top':
            cent_dev_angle = py.degrees(py.arctan2(-m.CenterYd,-m.CenterXd))
        else:
            cent_dev_angle = py.degrees(py.arctan2(-m.CenterYd,m.CenterXd))
        #0.08 is threshold, as this rotation around the center leads to more than 100 um deveiation at the sensor corner
        c = 'b'
        if abs(angle_dev)>0.08: c='r'
        drawCirc(ax,(m.CenterXd**2 + m.CenterYd**2)**0.5*1000,m.CenterXn,m.CenterYn,cent_dev_angle,-angle_dev*500,color_=c)

#        drawCirc(ax,100,m.CenterXn,m.CenterYn,0,angle*100)

    module['angle_dev'] = angle_devs

    py.xlabel('mm')
    py.ylabel('mm')
    py.legend()
    py.title(Dee_name+', Module positions, '+s+' side')
    py.xlim([-1100,1100])
    py.ylim([-50,1100])
    ax.set_aspect(1)
    if s=='Top': ax.invert_xaxis()
    ax.invert_yaxis()
    py.savefig('../'+Dee_name+'/plots/2S_positions_'+s+'.png',dpi=600)
    py.savefig('../'+Dee_name+'/plots/2S_positions_'+s+'.pdf')


    full_disk_dfs.append(module.copy())


#print(full_disk_dfs)

full_disk = pd.concat(full_disk_dfs, ignore_index=True)

#sort by nominal (cad?) values
full_disk['Radius'] = np.sqrt(full_disk['CenterXn']**2 + full_disk['CenterYn']**2)

full_disk = full_disk.sort_values(by='Radius').reset_index(drop=True)

tolerance = 50.0  # different ring should be away more than, let's say, 50 mm
ring_indices = []

current_ring = 0
if '-E-' in Dee_name:
    current_ring = 12
else:
    current_ring = 11

ref_radius = full_disk.loc[0, 'Radius']
ring_indices.append(current_ring)

for i in range(1, len(full_disk)):
    radius = full_disk.loc[i, 'Radius']
    if abs(radius - ref_radius) > tolerance:
        current_ring += 2
        ref_radius = radius
    ring_indices.append(current_ring)

full_disk['RingIndex'] = ring_indices

#sort
angle = np.arctan2(full_disk['CenterXn'], full_disk['CenterYn'])
angle_shift = np.pi / 4
#adjusted_angle = (angle - angle_shift) % (2 * np.pi)
adjusted_angle = - (angle - angle_shift)
#angle = (-angle) % (2 * np.pi)
full_disk['Angle'] = adjusted_angle

full_disk = full_disk.sort_values(by=['RingIndex', 'Angle']).reset_index(drop=True)
full_disk['ModuleNumber'] = full_disk.groupby('RingIndex').cumcount() + 1

#columns_to_print = ['RingIndex', 'Radius', 'ModuleNumber', 'Angle', 'CenterXn', 'CenterXm', 'CenterXd', 'CenterYn', 'CenterYm', 'CenterYd', 'angle_dev']
columns_to_print = ['RingIndex', 'ModuleNumber', 'CenterXn', 'CenterXm', 'CenterYn', 'CenterYm', 'CenterXd', 'CenterYd', 'angle_dev']
print(full_disk[columns_to_print].to_string(index=False))

full_disk.to_csv(os.path.join('..', Dee_name, 'plots/2S_positions_sorted.csv'), columns=columns_to_print, index=False)

#py.show()
