Summary:	X-Conquest scriptable multiplayer wargame
Summary(pl.UTF-8):   X-Conquest - skryptowalna gra wojenna dla wielu graczy
Name:		xconq
Version:	7.2.2
Release:	1
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
X-conquest is a multi-player strategic wargame. Newer releases of
xconq do support a scripting engine as well as many other
enhancements.

%description -l pl.UTF-8
X-conquest to strategiczna gra wojenna dla wielu graczy. Nowe wersje
xconq obsługują silnik skryptowy oraz wiele innych rozszerzeń.

%prep
%setup -q

%build
%configure
%{__make} \
	datadir=/var/lib/games/xconq \
	docdir=%{_docdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/lib/games

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	datadir=$RPM_BUILD_ROOT/var/lib/games/xconq \
	docdir=$RPM_BUILD_ROOT%{_docdir}

%{__make} -C doc install-info \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README INSTALL NEWS
%attr(755,root,root) %{_bindir}/xconq
%attr(755,root,root) %{_bindir}/imf2x
%attr(755,root,root) %{_bindir}/x2imf
%attr(755,root,root) %{_bindir}/xshowimf
%attr(755,root,root) %{_bindir}/cconq
%{_mandir}/man6/xconq.6*
%{_mandir}/man6/cconq.6*
/var/lib/games/xconq
%{_infodir}/xcdesign.info*
%{_infodir}/xconq.info*
