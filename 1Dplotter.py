import os as os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import datareaders as dr

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['legend.handlelength']=4
mpl.rcParams['legend.fontsize']=16
mpl.rcParams['legend.frameon']=False
mpl.rcParams['axes.labelsize']=20

number_of_contributions = 3
sim_names = range(number_of_contributions)
plotcolors = range(number_of_contributions)
time = range(number_of_contributions)
rshk = range(number_of_contributions)
massaccretion = range(number_of_contributions)
lumnue = range(number_of_contributions)
lumanue = range(number_of_contributions)
lumnux = range(number_of_contributions)
aveenue = range(number_of_contributions)
aveeanue = range(number_of_contributions)
aveenux = range(number_of_contributions)

cc = 0
#give a name for the legends
sim_names[cc] = r"${\tt GR1D-GREP}$"
plotcolors[cc] = 'k'
#scalars
time[cc],rshk[cc],massaccretion[cc],lumnue[cc],lumanue[cc],lumnux[cc],aveenue[cc],aveeanue[cc],aveenux[cc] = dr.get_GR1DData("GR1Ddata")

cc = cc + 1
#give a name for the legends
sim_names[cc] = r"${\tt GR1D-GR}$"
plotcolors[cc] = 'grey'
#scalars
time[cc],rshk[cc],massaccretion[cc],lumnue[cc],lumanue[cc],lumnux[cc],aveenue[cc],aveeanue[cc],aveenux[cc] = dr.get_GR1DData("GR1Ddata_GR")


cc = cc + 1
#give a name for the legends
sim_names[cc] = r"${\tt FLASH}$"
plotcolors[cc] = 'g'
#scalars
time[cc],rshk[cc],massaccretion[cc],lumnue[cc],lumanue[cc],lumnux[cc],aveenue[cc],aveeanue[cc],aveenux[cc] = dr.get_FLASHData()

#template
#cc = cc + 1
##give a name for the legends
#sim_names[cc] = "myCode"
#plotcolors[cc] = 'g'
##read in scalars, must supply reader in datareader.py
#time[cc],rshk[cc],massaccretion[cc],lumnue[cc],lumanue[cc],lumnux[cc],aveenue[cc],aveeanue[cc],aveenux[cc] = dr.get_myCodeData()


#plt shock
for i in range(number_of_contributions):
    plt.plot(time[i],rshk[i],label=sim_names[i],color=plotcolors[i])

plt.legend(loc='upper right')
plt.xlabel("$t_{\mathrm{pb}}$ [s]")
plt.ylabel("Shock Radius [km]")
plt.xlim((-0.05,0.5))
plt.ylim((0.0,160.))
plt.savefig("./plots/shock_radius.pdf")

plt.clf()

#plt mass accretion
for i in range(number_of_contributions):
    plt.plot(time[i],massaccretion[i],label=sim_names[i],color=plotcolors[i])

plt.legend(loc='upper right')
plt.xlabel("$t_{\mathrm{pb}}$ [s]")
plt.ylabel(r"Mass Accretion Rate at 500km [M$_\odot$/s]")
plt.xlim((-0.05,0.5))
plt.ylim((0.0,8.))
plt.savefig("./plots/mass_accretion.pdf")

plt.clf()

#plt lums
plot_lines = []
plot_names = []
for i in range(number_of_contributions):
    l1, = plt.plot(time[i],lumnue[i],label=sim_names[i],color=plotcolors[i],linestyle='-')
    plt.plot(time[i],lumanue[i],color=plotcolors[i],linestyle='-.')
    plt.plot(time[i],lumnux[i],color=plotcolors[i],linestyle='--')
    plot_lines.append(l1)
    plot_names.append(sim_names[i])

black_line1, = plt.plot([], [], color='k', linestyle='-')
black_line2, = plt.plot([], [], color='k', linestyle='-.')
black_line3, = plt.plot([], [], color='k', linestyle='--')        
legend1 = plt.legend(plot_lines,plot_names,loc='upper right')
plt.legend([black_line1,black_line2,black_line3],[r"$\nu_e$",r"$\bar{\nu}_e$",r"$\nu_x$"],loc=(0.2,0.05))
plt.gca().add_artist(legend1)
    
plt.xlabel("$t_{\mathrm{pb}}$ [s]")
plt.ylabel(r"Luminosity [10$^{51}$ erg/s]")
plt.xlim((-0.05,0.55))
plt.ylim((0.0,90))
plt.savefig("./plots/lums.pdf")

plt.clf()

#plt enue, anue
plot_lines = []
plot_names = []
for i in range(number_of_contributions):
    l1, = plt.plot(time[i],aveenue[i],label=sim_names[i],color=plotcolors[i],linestyle='-')
    plt.plot(time[i],aveeanue[i],color=plotcolors[i],linestyle='-.')
    plot_lines.append(l1)
    plot_names.append(sim_names[i])

black_line1, = plt.plot([], [], color='k', linestyle='-')
black_line2, = plt.plot([], [], color='k', linestyle='-.')        
legend1 = plt.legend(plot_lines,plot_names,loc='upper left')
plt.legend([black_line1,black_line2],[r"$\nu_e$",r"$\bar{\nu}_e$"],loc="lower right")
plt.gca().add_artist(legend1)

plt.xlabel("$t_{\mathrm{pb}}$ [s]")
plt.ylabel(r"$\langle E_\nu \rangle$ [MeV]")
plt.xlim((-0.05,0.5))
plt.ylim((5.,20))
plt.savefig("./plots/avee_nue_anue.pdf")

plt.clf()

#plt enux
plot_lines = []
plot_names = []
for i in range(number_of_contributions):
    l1, = plt.plot(time[i],aveenux[i],color=plotcolors[i],linestyle='--')
    plot_lines.append(l1)
    plot_names.append(sim_names[i])

black_line, = plt.plot([], [], color='k', linestyle='--')        
legend1 = plt.legend(plot_lines,plot_names,loc='upper right')
plt.legend([black_line],[r"$\nu_x$"],loc="lower right")
plt.gca().add_artist(legend1)
plt.xlabel(r"$t_{\mathrm{pb}}$ [s]")
plt.ylabel(r"$\langle E_\nu \rangle$ [MeV]")
plt.xlim((-0.05,0.5))
plt.ylim((5.,25))
plt.savefig("./plots/avee_nux.pdf")
