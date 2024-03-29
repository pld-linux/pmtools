Summary:	Retrieve the DSDT from your BIOS
Summary(pl.UTF-8):	Narzędzie do odczytu DSDT z BIOS-u
Name:		pmtools
Version:	20110323
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://ftp.kernel.org/pub/linux/kernel/people/lenb/acpi/utils/%{name}-%{version}.tar.bz2
# Source0-md5:	9ed64a1c04bb9597257786de034a77a9
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

%description -l pl.UTF-8
DSDT to skrót od Differentiated System Description Table (różnicowa
tabela opisu systemu). Jest to tabela zawierająca różnicowy blok
definicji, dostarczający informacji o systemie bazowym i jego
konfiguracji. Jest zawsze umieszczany w przestrzeni nazw ACPI przez
system operacyjny w czasie startu. Niestety wielu producentów sprzętu
i OEM-ów nie ma możliwości dostarczania w pełni funkcjonalnych tabel
(nawet członkowie ACPI SIG).

%prep
%setup -q -n %{name}

%{__mv} madt/README README.madt

%build
%{__cc} %{rpmldflags} %{rpmcflags} -o madt/madt madt/madt.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install madt/madt $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.madt
%attr(755,root,root) %{_sbindir}/madt
