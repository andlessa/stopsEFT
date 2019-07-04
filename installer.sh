#!/bin/sh

homeDIR="$( pwd )"

#Get HepMC tarball
softsusy="softsusy-4.1.7.tar.gz"
echo -n "Install softsusy (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
  mkdir softsusy;
	tar -zxf $softsusy -C softsusy --strip-components 1;
	echo "Installing softsusy";
	cd softsusy;
  ./configure;
	make;
 cd ..;
fi

madgraph="MG5_aMC_v2.6.5.tar.gz"
URL=https://launchpad.net/mg5amcnlo/2.0/2.6.x/+download/$madgraph
echo -n "Install MadGraph (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
	mkdir MG5;
	echo "[installer] getting MadGraph5"; wget $URL 2>/dev/null || curl -O $URL; tar -zxf $madgraph -C MG5 --strip-components 1;
	rm $madgraph;
  cp ./mg5_configuration.txt MG5/input/;
fi


colliderbit="ColliderBit-1.3.1.tar.gz"
URL=https://gambit.hepforge.org/downloads/?f=ColliderBit%20(standalone)/$colliderbit
echo -n "Install ColliderBit (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
	mkdir ColliderBit;
	echo "[installer] getting ColliderBit"; wget $URL 2>/dev/null || curl -O $URL; tar -zxf $colliderbit -C ColliderBit --strip-components 1;
	rm $colliderbit;
  cd ColliderBit;
  mkdir build;
  cd build;
  cmake ..;
  make;
  make -j4 ColliderBit_standalone;
  make nulike;
  make pythia_8.212.EM;
fi
