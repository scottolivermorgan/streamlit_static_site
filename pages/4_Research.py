import streamlit as st
from helpers.helpers import load_css, research_card
from helpers.helpers import load_footer, load_navbar_style

load_navbar_style()


# Load css stylesheet
load_css("./assets/static/css/styles.css")

# Create two columns with a 50:50 width ratio
col1, col2 = st.columns(2)

with col1:
    research_card("./assets/static/images/research/nanorods.png",
                  "Metamaterials Fabricated by Self Assembly",

        "Vertically aligned monolayers of metallic nanorods have a wide \
                  range of applications as metamaterials or in surface enhanced Raman \
				  spectroscopy. However the fabrication of such structures using current \
				  top-down methods or through assembly on solid substrates is either \
				  difficult to scale up or have limited possibilities for further \
				  modification after assembly. The aim of this paper is to use the adsorption\
				  kinetics of cylindrical nanorods at a liquid interface as a novel route \
				  for assembling vertically aligned nanorod arrays that overcomes these problems.",
                  "https://pubs.rsc.org/en/content/articlehtml/2022/cp/d1cp05484h")

with col2:
    research_card("./assets/static/images/research/optoelectonic-switch.png",
                  "Optoelectronic Switches for Neuromorphic Computing",
                  "Optoelectronic switching memories are emerging as practical candidates for applications of optically tunable neuromorphic computing systems and artificial vision systems. Here, we report on the fabrication of an optoelectronic switching memory device based on semiconducting zinc oxide nanoparticles (ZnO NPs) embedded within a photoactive azobenzene polymer. The device shows electronic resistive switching and a reversible optical switching effect upon changing the polarization of the applied light",
                  "https://pubs.acs.org/doi/full/10.1021/acsapm.2c02034")

# Create two columns with a 50:50 width ratio
col3, col4 = st.columns(2)#

with col3:
    research_card("./assets/static/images/research/ellipsoids.png",
                  "Adsorbtion and Self Assembly",
                  "The adsorption of colloidal particles at liquid interfaces is of great importance scientifically and industrially, but the dynamics of the adsorption process is still poorly understood. In this paper we use a Langevin model to study the adsorption dynamics of ellipsoidal colloids at a liquid interface. Interfacial deformations are included by coupling our Langevin dynamics to a finite element model while transient contact line pinning due to nanoscale defects on the particle surface is encoded into our model by renormalizing particle friction coefficients and using dynamic contact angles relevant to the adsorption timescale",
                  "https://journals.aps.org/pre/abstract/10.1103/PhysRevE.103.042604")

with col4:
    research_card("./assets/static/images/research/nanorods.png",
                  "2D Programmable Materials",
                  "In recent years, self-assembly has emerged as a powerful tool for fabricating functional materials. Since self-assembly is fundamentally determined by the particle interactions in the system, if we can gain full control over these interactions, it would open the door for creating functional materials by design. In this paper, we exploit capillary interactions between colloidal particles at liquid interfaces to create two-dimensional (2D) materials where particle interactions and self-assembly can be fully programmed using particle shape alone.",
                  "https://www.pnas.org/doi/abs/10.1073/pnas.2401134121")

load_footer()