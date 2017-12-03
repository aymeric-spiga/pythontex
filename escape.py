import planets

import numpy as np
import matplotlib.pyplot as mpl

# This line configures matplotlib to show figures embedded in the notebook.

tabplanet = []
tabplanet.append("Mercury")
tabplanet.append("Venus")
tabplanet.append("Earth")
tabplanet.append("Mars")
tabplanet.append("Jupiter")
tabplanet.append("Saturn")
tabplanet.append("Pluto")

# This configures different colors for each plots
ax = mpl.gca()
pal = mpl.cm.get_cmap(name="spectral_r")
ax._get_lines.set_color_cycle([pal(i) for i in np.linspace(0,0.9,len(tabplanet))])

planet = planets.Planet()
for ppp in tabplanet:
  planet.ini(ppp)
  mpl.plot(planet.g,planet.lescape(),"s",label=planet.name)
    
## ligne Lescape > 100 (ratio interieur carre plus grand que 10)
## -- Lescape propor to masse molaire
mm = 1.  ; spe = r'$H$'    ; mpl.plot([0.1,100],[100/mm,100/mm],'k--',label=spe)  
mm = 18. ; spe = r'$H_2O$' ; mpl.plot([0.1,100],[100/mm,100/mm],'b-.',label=spe)


mpl.legend(loc="upper left")
mpl.xlabel(r'gravity (m s$^{-2}$)',fontsize="large")
mpl.ylabel(r'escape parameter $\lambda_e$',fontsize="large")
mpl.xscale("log") ; mpl.yscale("log")
#mpl.show()

mpl.savefig("escape.pdf")
