%bcond_with check
%global debug_package %{nil}

%global crate chrono

Name:           rust-%{crate}
Version:        0.4.19
Release:        2
Summary:        Date and time library for Rust

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/chrono
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(libc/default) >= 0.2.69 with crate(libc/default) < 0.3.0)
BuildRequires:  (crate(num-integer) >= 0.1.36 with crate(num-integer) < 0.2.0)
BuildRequires:  (crate(num-traits) >= 0.2.0 with crate(num-traits) < 0.3.0)
BuildRequires:  (crate(time/default) >= 0.1.43 with crate(time/default) < 0.2.0)
%if %{with check}
BuildRequires:  (crate(bincode/default) >= 1.3.0 with crate(bincode/default) < 2.0.0)
BuildRequires:  (crate(doc-comment/default) >= 0.3.0 with crate(doc-comment/default) < 0.4.0)
BuildRequires:  (crate(num-iter) >= 0.1.35 with crate(num-iter) < 0.2.0)
BuildRequires:  (crate(serde_derive) >= 1.0.0 with crate(serde_derive) < 2.0.0)
BuildRequires:  (crate(serde_json/default) >= 1.0.0 with crate(serde_json/default) < 2.0.0)
%endif
%endif

# Initial patched metadata
# * No wasm
Patch0:		chrono-fix-metadata.diff
Patch1:		chrono-0.4.19-allow-newer-bincode.patch

%global _description %{expand:
Date and time library for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(chrono) = 0.4.19
Requires:       cargo
Requires:       (crate(num-integer) >= 0.1.36 with crate(num-integer) < 0.2.0)
Requires:       (crate(num-traits) >= 0.2.0 with crate(num-traits) < 0.3.0)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(chrono/default) = 0.4.19
Requires:       cargo
Requires:       crate(chrono) = 0.4.19
Requires:       crate(chrono/clock) = 0.4.19
Requires:       crate(chrono/oldtime) = 0.4.19
Requires:       crate(chrono/std) = 0.4.19

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+__doctest-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(chrono/__doctest) = 0.4.19
Requires:       cargo
Requires:       crate(chrono) = 0.4.19

%description -n %{name}+__doctest-devel %{_description}

This package contains library source intended for building other packages
which use "__doctest" feature of "%{crate}" crate.

%files       -n %{name}+__doctest-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+__internal_bench-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(chrono/__internal_bench) = 0.4.19
Requires:       cargo
Requires:       crate(chrono) = 0.4.19

%description -n %{name}+__internal_bench-devel %{_description}

This package contains library source intended for building other packages
which use "__internal_bench" feature of "%{crate}" crate.

%files       -n %{name}+__internal_bench-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(chrono/alloc) = 0.4.19
Requires:       cargo
Requires:       crate(chrono) = 0.4.19

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages
which use "alloc" feature of "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clock-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(chrono/clock) = 0.4.19
Requires:       cargo
Requires:       (crate(libc/default) >= 0.2.69 with crate(libc/default) < 0.3.0)
Requires:       crate(chrono) = 0.4.19
Requires:       crate(chrono/std) = 0.4.19

%description -n %{name}+clock-devel %{_description}

This package contains library source intended for building other packages
which use "clock" feature of "%{crate}" crate.

%files       -n %{name}+clock-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+js-sys-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(chrono/js-sys) = 0.4.19
Requires:       cargo
Requires:       (crate(js-sys/default) >= 0.3.0 with crate(js-sys/default) < 0.4.0)
Requires:       crate(chrono) = 0.4.19

%description -n %{name}+js-sys-devel %{_description}

This package contains library source intended for building other packages
which use "js-sys" feature of "%{crate}" crate.

%files       -n %{name}+js-sys-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+libc-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(chrono/libc) = 0.4.19
Requires:       cargo
Requires:       (crate(libc/default) >= 0.2.69 with crate(libc/default) < 0.3.0)
Requires:       crate(chrono) = 0.4.19

%description -n %{name}+libc-devel %{_description}

This package contains library source intended for building other packages
which use "libc" feature of "%{crate}" crate.

%files       -n %{name}+libc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+oldtime-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(chrono/oldtime) = 0.4.19
Requires:       cargo
Requires:       (crate(time/default) >= 0.1.43 with crate(time/default) < 0.2.0)
Requires:       crate(chrono) = 0.4.19

%description -n %{name}+oldtime-devel %{_description}

This package contains library source intended for building other packages
which use "oldtime" feature of "%{crate}" crate.

%files       -n %{name}+oldtime-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pure-rust-locales-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(chrono/pure-rust-locales) = 0.4.19
Requires:       cargo
Requires:       (crate(pure-rust-locales/default) >= 0.5.2 with crate(pure-rust-locales/default) < 0.6.0)
Requires:       crate(chrono) = 0.4.19

%description -n %{name}+pure-rust-locales-devel %{_description}

This package contains library source intended for building other packages
which use "pure-rust-locales" feature of "%{crate}" crate.

%files       -n %{name}+pure-rust-locales-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rustc-serialize-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(chrono/rustc-serialize) = 0.4.19
Requires:       cargo
Requires:       (crate(rustc-serialize/default) >= 0.3.20 with crate(rustc-serialize/default) < 0.4.0)
Requires:       crate(chrono) = 0.4.19

%description -n %{name}+rustc-serialize-devel %{_description}

This package contains library source intended for building other packages
which use "rustc-serialize" feature of "%{crate}" crate.

%files       -n %{name}+rustc-serialize-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(chrono/serde) = 0.4.19
Requires:       cargo
Requires:       (crate(serde) >= 1.0.99 with crate(serde) < 2.0.0)
Requires:       crate(chrono) = 0.4.19

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(chrono/std) = 0.4.19
Requires:       cargo
Requires:       crate(chrono) = 0.4.19

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+time-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(chrono/time) = 0.4.19
Requires:       cargo
Requires:       (crate(time/default) >= 0.1.43 with crate(time/default) < 0.2.0)
Requires:       crate(chrono) = 0.4.19

%description -n %{name}+time-devel %{_description}

This package contains library source intended for building other packages
which use "time" feature of "%{crate}" crate.

%files       -n %{name}+time-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unstable-locales-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(chrono/unstable-locales) = 0.4.19
Requires:       cargo
Requires:       (crate(pure-rust-locales/default) >= 0.5.2 with crate(pure-rust-locales/default) < 0.6.0)
Requires:       crate(chrono) = 0.4.19
Requires:       crate(chrono/alloc) = 0.4.19

%description -n %{name}+unstable-locales-devel %{_description}

This package contains library source intended for building other packages
which use "unstable-locales" feature of "%{crate}" crate.

%files       -n %{name}+unstable-locales-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+wasm-bindgen-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(chrono/wasm-bindgen) = 0.4.19
Requires:       cargo
Requires:       (crate(wasm-bindgen/default) >= 0.2.0 with crate(wasm-bindgen/default) < 0.3.0)
Requires:       crate(chrono) = 0.4.19

%description -n %{name}+wasm-bindgen-devel %{_description}

This package contains library source intended for building other packages
which use "wasm-bindgen" feature of "%{crate}" crate.

%files       -n %{name}+wasm-bindgen-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+wasmbind-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(chrono/wasmbind) = 0.4.19
Requires:       cargo
Requires:       (crate(js-sys/default) >= 0.3.0 with crate(js-sys/default) < 0.4.0)
Requires:       (crate(wasm-bindgen/default) >= 0.2.0 with crate(wasm-bindgen/default) < 0.3.0)
Requires:       crate(chrono) = 0.4.19

%description -n %{name}+wasmbind-devel %{_description}

This package contains library source intended for building other packages
which use "wasmbind" feature of "%{crate}" crate.

%files       -n %{name}+wasmbind-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
