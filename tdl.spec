Summary: A to-do list manager
Name: tdl
Version: 1.6-pre1
Release: 1
Copyright: GPL
Source: tdl-%{version}.tar.gz
Group: Applications/Utilities
Packager: Richard P. Curnow <rc@rc0.org.uk>
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(id -u -n)
Requires: readline

%description
tdl is a console to-do list manager.  You can run its subcommands direct from
the command line, or enter an interactive mode which uses the readline library.

%prep
%setup -q

%build
configure
make %{?_smp_mflags} CC=gcc CFLAGS=-O2 prefix=%{_prefix}
make %{?_smp_mflags} tdl.txt prefix=%{_prefix}
make %{?_smp_mflags} tdl.info prefix=%{_prefix}
make %{?_smp_mflags} tdl.html prefix=%{_prefix}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} prefix=%{_prefix} bindir=%{buildroot}%{_bindir} mandir=%{buildroot}%{_mandir}
mkdir -p %{buildroot}%{_infodir}
cp tdl.info* %{buildroot}/%{_infodir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README tdl.txt tdl.html
%{_bindir}/tdl*
%{_mandir}/man[^3]/*
%{_infodir}/*

