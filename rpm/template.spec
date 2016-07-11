Name:           ros-indigo-image-geometry
Version:        1.11.13
Release:        0%{?dist}
Summary:        ROS image_geometry package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/image_geometry
Source0:        %{name}-%{version}.tar.gz

Requires:       opencv-devel
Requires:       opencv-python
Requires:       ros-indigo-sensor-msgs
BuildRequires:  opencv-devel
BuildRequires:  opencv-python
BuildRequires:  ros-indigo-catkin >= 0.5.68
BuildRequires:  ros-indigo-sensor-msgs

%description
`image_geometry` contains C++ and Python libraries for interpreting images
geometrically. It interfaces the calibration parameters in
sensor_msgs/CameraInfo messages with OpenCV functions such as image
rectification, much as cv_bridge interfaces ROS sensor_msgs/Image with OpenCV
data types.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Jul 11 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.11.13-0
- Autogenerated by Bloom

* Thu Mar 10 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.11.12-0
- Autogenerated by Bloom

* Sun Jan 31 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.11.11-0
- Autogenerated by Bloom

* Sat Jan 16 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.11.10-0
- Autogenerated by Bloom

* Sun Nov 29 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.11.9-0
- Autogenerated by Bloom

* Wed Jul 15 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 1.11.8-0
- Autogenerated by Bloom

