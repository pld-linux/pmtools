Summary:	Retrieve the DSDT from your BIOS
Summary(pl):	Narzêdzie do odczytu DSDT z BIOS-u
Name:		pmtools
Version:	20061026
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://ftp.kernel.org/pub/linux/kernel/people/lenb/acpi/utils/%{name}-%{version}.tar.bz2
# Source0-md5:	a64834987d23e35c90a80c1ca0c3e2ae
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
DSDT to skrót od Differentiated System Description Table (ró¿nicowa
tabela opisu systemu). Jest to tabela zawieraj±ca ró¿nicowy blok
definicji, dostarczaj±cy informacji o systemie bazowym i jego
konfiguracji. Jest zawsze umieszczany w przestrzeni nazw ACPI przez
system operacyjny w czasie startu. Niestety wielu producentów sprzêtu
i OEM-ów nie ma mo¿liwo¶ci dostarczania w pe³ni funkcjonalnych tabel
(nawet cz³onkowie ACPI SIG).

%prep
%setup -q

mv -f madt/README README.madt

%build
%{__make} -C acpidump \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -W -pedantic -D_LINUX -DDEFINE_ALTERNATE_TYPES  -I../include"

%{__cc} %{rpmldflags} %{rpmcflags} -o madt/madt madt/madt.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install acpidump/{acpidump,acpitbl,acpixtract} $RPM_BUILD_ROOT%{_sbindir}
install madt/madt $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.madt
%attr(755,root,root) %{_sbindir}/*
