%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	PackageUpdate
%define		_status		beta
%define		_pearname	PEAR_PackageUpdate

Summary:	%{_pearname} - a simple way to update packages at runtime
Summary(pl):	%{_pearname} - prosty spos�b do aktualizacji paczek w czasie dzia�ania aplikacji
Name:		php-pear-%{_pearname}
Version:	0.4.2
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1bc0869e21d749071f58213ef4c9f8a1
URL:		http://pear.php.net/package/PEAR_PackageUpdate/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
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

%description -l pl
PEAR_PackageUpdate (PPU) zosta� zaprojektowany aby umo�liwi�
developerom do��czenie w prosty spos�b automatycznej aktualizacji
innych pakiet�w PEAR lub aplikacji korzystaj�cych ze sposobu
instalacji PEAR. PPU sprawdzi czy jest dost�pna nowa wersja i zapyta
u�ytkownika czy chcieliby zaktualizowa� pakiet. PPU korzysta z PEAR do
komunikacji z serwerem kana��w oraz do wykonania aktualizacji.

PPU pozwala u�ytkownikowi ko�cowemu na pewn� kontrol� kiedy maj� by�
powiadamiania o nowych aktualizacjach. Preferencje PPU pozwalaj�
u�ytkownikowi na pomini�cie pewnych rodzaj�w aktualizacji (poprawki
b��d�w, drobne wydania), czy konkretnych status�w (devel, alpha,
itp.), czy polecenie PPU aby nie pyta� do czasu kolejnej wersji.

PPU jest tylko silnikiem do aktualizacji pakiet�w. Nie powinien by�
u�yty bezpo�rednio. Zamiast tego, pakiety takie jak
PEAR_PackageUpdate_GTK2 powinny by� u�yte.

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
