Summary: X-Conquest scriptable multiplayer wargame
Name: xconq
Version: 7.2.2
Release: 1
Group: X11/Games/Strategy
Source: xconq-%{PACKAGE_VERSION}.tar.gz
Copyright: GPL
BuildRoot: /tmp/xconq-root

%description
This is the newest release of xconq packaged for RedHat Linux.  X-conquest
is a multi-player strategic wargame.  Newer releases of xconq do support
a scripting engine as well as many other enhancements.  Many people will
probably debate my choice of file locations.

%prep
%setup
./configure --prefix=/usr
%build
make datadir=/var/lib/games/xconq docdir=/usr/doc

%install
mkdir -p $RPM_BUILD_ROOT/var/lib/games
make prefix=$RPM_BUILD_ROOT/usr datadir=$RPM_BUILD_ROOT/var/lib/games/xconq docdir=$RPM+BUILD_ROOT/usr/doc install
cd doc ; make prefix=$RPM_BUILD_ROOT/usr install-info
%files
%doc COPYING README INSTALL NEWS

/usr/bin/xconq
/usr/bin/imf2x
/usr/bin/x2imf
/usr/bin/xshowimf
/usr/bin/cconq
/usr/man/man6/xconq.6
/usr/man/man6/cconq.6
/var/lib/games/xconq
/usr/info/xcdesign.info
/usr/info/xcdesign.info-1
/usr/info/xcdesign.info-10
/usr/info/xcdesign.info-11
/usr/info/xcdesign.info-12
/usr/info/xcdesign.info-13
/usr/info/xcdesign.info-2
/usr/info/xcdesign.info-3
/usr/info/xcdesign.info-4
/usr/info/xcdesign.info-5
/usr/info/xcdesign.info-6
/usr/info/xcdesign.info-7
/usr/info/xcdesign.info-8
/usr/info/xcdesign.info-9
/usr/info/xconq.info
/usr/info/xconq.info-1
/usr/info/xconq.info-2
/usr/info/xconq.info-3
/usr/info/xconq.info-4
/usr/info/xconq.info-5
