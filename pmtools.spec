Summary:	Retrieve the DSDT from your BIOS
Summary(pl.UTF-8):	Narzędzie do odczytu DSDT z BIOS-u
Name:		pmtools
Version:	20110323
Release:	1
License:	GPL
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

mv -f madt/README README.madt

%build
%{__make} -C acpidump \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -Wstrict-prototypes -Wdeclaration-after-statement -D_LINUX -DDEFINE_ALTERNATE_TYPES -I../include"

%{__make} -C acpixtract \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -Wstrict-prototypes -D_LINUX -DACPI_APPLICATION -I../include"

%{__cc} %{rpmldflags} %{rpmcflags} -o madt/madt madt/madt.c
%{__cc} %{rpmldflags} %{rpmcflags} -o turbostat/turbostat turbostat/turbostat.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install acpidump/acpidump acpixtract/acpixtract madt/madt turbostat/turbostat \
	$RPM_BUILD_ROOT%{_sbindir}
install turbostat/turbostat.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.madt
%attr(755,root,root) %{_sbindir}/acpidump
%attr(755,root,root) %{_sbindir}/acpixtract
%attr(755,root,root) %{_sbindir}/madt
%attr(755,root,root) %{_sbindir}/turbostat
%{_mandir}/man8/turbostat.8*
