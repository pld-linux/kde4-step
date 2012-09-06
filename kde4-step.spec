%define		_state		stable
%define		orgname		step

Summary:	K Desktop Environment - Interactive Physical Simulator
Summary(pl.UTF-8):	K Desktop Environment - interaktywny symulator fizyczny
Name:		kde4-step
Version:	4.9.1
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	0e36c3f684e98025d2156fc8de64c174
URL:		http://www.kde.org/
BuildRequires:	cln-devel
BuildRequires:	eigen
BuildRequires:	gsl-devel
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libqalculate-devel >= 0.9.5
Obsoletes:	kde4-kdeedu-step < 4.7.0
Obsoletes:	step <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Step is an interactive physical simulator.

It works like this: you place some bodies on the scene, add some
forces such as gravity or springs, then click "Simulate" and Step
shows you how your scene will evolve according to the laws of physics.

You can change every property of bodies/forces in your experiment
(even during simulation) and see how this will change evolution of the
experiment. With Step you can not only learn but feel how physics
works!

%description -l pl.UTF-8
Step to interaktywny symulator fizyczny.

Działa w ten sposób: umieszcza się na scenie jakieś ciała, dodaje siły
takie jak grawitacja czy sprężyny, a następnie wciska przycisk
"Symuluj" - a Step pokazuje, jak scena będzie się zmieniała zgodnie z
prawami fizyki.

W ramach eksperymentu można zmieniać każdą właściwość ciał/sił (nawet
podczas symulacji) i obserwować, jak zmieni to jego przebieg. Przy
użyciu Stepa można nie tylko nauczyć się, ale i poczuć, jak działa
fizyka.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/step
%{_datadir}/apps/step
%{_datadir}/config.kcfg/step.kcfg
%{_datadir}/config/step.knsrc
%{_desktopdir}/kde4/step.desktop
%{_iconsdir}/hicolor/*/apps/step.png
