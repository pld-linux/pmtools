Summary:	Retrieve the DSDT from your BIOS
Summary(pl):	Narz�dzie do odczytu DSDT z BIOS-u
Name:		pmtools
Version:	20031210
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://ftp.kernel.org/pub/linux/kernel/people/lenb/acpi/utils/%{name}-%{version}.tar.bz2
# Source0-md5:	7d482ab86410f3f8c30a9fba5d660f32
URL:		http://acpi.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DSDT is an acronym for Differentiated System Description Table. This
table contains the Differentiated Definition Block, which supplies the
information and configuration information about the base system. It is
always inserted into the ACPI Namespace by the OS at boot time.
Unfortunately, many hardware vendors and OEMs are not capable of
supplying fully functional tables (not even the members of the ACPI
SIG)

%description -l pl
DSDT to skr�t od Differentiated System Description Table (r�nicowa
tabela opisu systemu). Jest to tabela zawieraj�ca r�nicowy blok
definicji, dostarczaj�cy informacji o systemie bazowym i jego
konfiguracji. Jest zawsze umieszczany w przestrzeni nazw ACPI przez
system operacyjny w czasie startu. Niestety wielu producent�w sprz�tu
i OEM-�w nie ma mo�liwo�ci dostarczania w pe�ni funkcjonalnych tabel
(nawet cz�onkowie ACPI SIG).

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -W -pedantic"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README AUTHORS
%attr(755,root,root) %{_sbindir}/*