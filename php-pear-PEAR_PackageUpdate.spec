%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	PackageUpdate
%define		_status		beta
%define		_pearname	PEAR_PackageUpdate

Summary:	%{_pearname} - a simple way to update packages at runtime
Summary(pl.UTF-8):   %{_pearname} - prosty sposób do aktualizacji paczek w czasie działania aplikacji
Name:		php-pear-%{_pearname}
Version:	0.5.1
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6ab897e977f7c885292d38b7f8ea9869
URL:		http://pear.php.net/package/PEAR_PackageUpdate/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR >= 1.4.8
Requires:	php-pear-PEAR >= 1:1.4.-0.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PEAR_PackageUpdate (PPU) is designed to allow developers to easily
include auto updating features for other packages and PEAR installable
applications. PPU will check to see if a new version of a package is
available and then ask the user if they would like to update the
package. PPU uses PEAR to communicate with the channel server and to
execute the update.

PPU allows the end user to take some control over when they are
notified about new releases. The PPU Preferences allow a user to tell
PPU not to ask about certain types of releases (bug fixes, minor
releases, etc.), not to ask about certain release states (devel,
alpha, etc.), not to ask until the next release or not to ask again.

PPU is just an engine for package updating. It should not be used
directly. Instead one of the driver packages such as
PEAR_PackageUpdate_Gtk2 should be used depending on the application or
other package.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
PEAR_PackageUpdate (PPU) został zaprojektowany aby umożliwić
developerom dołączenie w prosty sposób automatycznej aktualizacji
innych pakietów PEAR lub aplikacji korzystających ze sposobu
instalacji PEAR. PPU sprawdzi czy jest dostępna nowa wersja i zapyta
użytkownika czy chcieliby zaktualizować pakiet. PPU korzysta z PEAR do
komunikacji z serwerem kanałów oraz do wykonania aktualizacji.

PPU pozwala użytkownikowi końcowemu na pewną kontrolę kiedy mają być
powiadamiania o nowych aktualizacjach. Preferencje PPU pozwalają
użytkownikowi na pominięcie pewnych rodzajów aktualizacji (poprawki
błędów, drobne wydania), czy konkretnych statusów (devel, alpha,
itp.), czy polecenie PPU aby nie pytał do czasu kolejnej wersji.

PPU jest tylko silnikiem do aktualizacji pakietów. Nie powinien być
użyty bezpośrednio. Zamiast tego, pakiety takie jak
PEAR_PackageUpdate_GTK2 powinny być użyte.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PEAR/PackageUpdate.php
