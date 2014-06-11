import string

api_server_conf_template = string.Template("""
[DEFAULTS]
ifmap_server_ip=$__contrail_ifmap_server_ip__
ifmap_server_port=$__contrail_ifmap_server_port__
ifmap_username=$__contrail_ifmap_username__
ifmap_password=$__contrail_ifmap_password__
redis_server_port=6379
redis_server_ip=$__contrail_redis_server_ip__
cassandra_server_list=$__contrail_cassandra_server_list__
listen_ip_addr=$__contrail_listen_ip_addr__
listen_port=$__contrail_listen_port__
auth=keystone
multi_tenancy=$__contrail_multi_tenancy__
log_file=$__contrail_log_file__
disc_server_ip=$__contrail_disc_server_ip__
disc_server_port=$__contrail_disc_server_port__
collectors=$__contrail_collectors__

[SECURITY]
use_certs=$__contrail_use_certs__
keyfile=$__contrail_keyfile_location__
certfile=$__contrail_certfile_location__
ca_certs=$__contrail_cacertfile_location__

[KEYSTONE]
auth_host=$__contrail_openstack_ip__
auth_protocol=http
auth_port=35357
admin_user=$__contrail_admin_user__
admin_password=$__contrail_admin_password__
admin_tenant_name=$__contrail_admin_tenant_name__
admin_token = $__contrail_admin_token__
$__contrail_memcached_opt__
""")

quantum_conf_template = string.Template("""
[APISERVER]
api_server_ip = $__contrail_api_server_ip__
api_server_port = $__contrail_api_server_port__
multi_tenancy = $__contrail_multi_tenancy__
contrail_extensions = ipam:neutron_plugin_contrail.plugins.opencontrail.contrail_plugin_ipam.NeutronPluginContrailIpam,policy:neutron_plugin_contrail.plugins.opencontrail.contrail_plugin_policy.NeutronPluginContrailPolicy,route-table:neutron_plugin_contrail.plugins.opencontrail.contrail_plugin_vpc.NeutronPluginContrailVpc

[KEYSTONE]
;auth_url = http://$__contrail_keystone_ip__:35357/v2.0
;admin_token = $__contrail_admin_token__
admin_user=$__contrail_admin_user__
admin_password=$__contrail_admin_password__
admin_tenant_name=$__contrail_admin_tenant_name__
""")

schema_transformer_conf_template = string.Template("""
[DEFAULTS]
ifmap_server_ip=$__contrail_ifmap_server_ip__
ifmap_server_port=$__contrail_ifmap_server_port__
ifmap_username=$__contrail_ifmap_username__
ifmap_password=$__contrail_ifmap_password__
api_server_ip=$__contrail_api_server_ip__
api_server_port=$__contrail_api_server_port__
zk_server_ip=$__contrail_zookeeper_server_ip__
zk_server_port=$__contrail_zookeeper_server_port__
log_file=$__contrail_log_file__
cassandra_server_list=$__contrail_cassandra_server_list__
disc_server_ip=$__contrail_disc_server_ip__
disc_server_port=$__contrail_disc_server_port__
collectors=$__contrail_collectors__

[SECURITY]
use_certs=$__contrail_use_certs__
keyfile=$__contrail_keyfile_location__
certfile=$__contrail_certfile_location__
ca_certs=$__contrail_cacertfile_location__

[KEYSTONE]
admin_user=$__contrail_admin_user__
admin_password=$__contrail_admin_password__
admin_tenant_name=$__contrail_admin_tenant_name__
""")

svc_monitor_conf_template = string.Template("""
[DEFAULTS]
ifmap_server_ip=$__contrail_ifmap_server_ip__
ifmap_server_port=$__contrail_ifmap_server_port__
ifmap_username=$__contrail_ifmap_username__
ifmap_password=$__contrail_ifmap_password__
api_server_ip=$__contrail_api_server_ip__
api_server_port=$__contrail_api_server_port__
zk_server_ip=$__contrail_zookeeper_server_ip__
zk_server_port=$__contrail_zookeeper_server_port__
log_file=$__contrail_log_file__
cassandra_server_list=$__contrail_cassandra_server_list__
disc_server_ip=$__contrail_disc_server_ip__
disc_server_port=$__contrail_disc_server_port__
collectors=$__contrail_collectors__

[SECURITY]
use_certs=$__contrail_use_certs__
keyfile=$__contrail_keyfile_location__
certfile=$__contrail_certfile_location__
ca_certs=$__contrail_cacertfile_location__

[KEYSTONE]
auth_host=$__contrail_openstack_ip__
admin_user=$__contrail_admin_user__
admin_password=$__contrail_admin_password__
admin_tenant_name=$__contrail_admin_tenant_name__
""")

bgp_param_template = string.Template("""
IFMAP_SERVER=$__contrail_ifmap_srv_ip__
IFMAP_PORT=$__contrail_ifmap_srv_port__
IFMAP_USER=$__contrail_ifmap_usr__
IFMAP_PASWD=$__contrail_ifmap_paswd__
COLLECTOR=$__contrail_collector__
COLLECTOR_PORT=$__contrail_collector_port__
DISCOVERY=$__contrail_discovery_ip__
HOSTNAME=$__contrail_hostname__
HOSTIP=$__contrail_host_ip__
BGP_PORT=$__contrail_bgp_port__
CERT_OPTS=$__contrail_cert_ops__
CONTROL_LOGFILE=$__contrail_logfile__
LOG_LOCAL=$__contrail_log_local__
""")

dns_param_template = string.Template("""
IFMAP_SERVER=$__contrail_ifmap_srv_ip__
IFMAP_PORT=$__contrail_ifmap_srv_port__
IFMAP_USER=$__contrail_ifmap_usr__
IFMAP_PASWD=$__contrail_ifmap_paswd__
COLLECTOR=$__contrail_collector__
COLLECTOR_PORT=$__contrail_collector_port__
DISCOVERY=$__contrail_discovery_ip__
HOSTIP=$__contrail_host_ip__
CERT_OPTS=$__contrail_cert_ops__
DNS_LOGFILE=$__contrail_logfile__
LOG_LOCAL=$__contrail_log_local__
""")


discovery_conf_template = string.Template("""
[DEFAULTS]
zk_server_ip=127.0.0.1
zk_server_port=$__contrail_zk_server_port__
listen_ip_addr=$__contrail_listen_ip_addr__
listen_port=$__contrail_listen_port__
log_local=$__contrail_log_local__
log_file=$__contrail_log_file__

# minimim time to allow client to cache service information (seconds)
ttl_min=300

# maximum time to allow client to cache service information (seconds)
ttl_max=1800

# maximum hearbeats to miss before server will declare publisher out of
# service. 
hc_max_miss=3

# use short TTL for agressive rescheduling if all services are not up
ttl_short=1

######################################################################
# Other service specific knobs ...
 
# use short TTL for agressive rescheduling if all services are not up
# ttl_short=1
 
# specify policy to use when assigning services
# policy = [load-balance | round-robin | fixed]
######################################################################
""")

vizd_param_template = string.Template("""
CASSANDRA_SERVER_LIST=$__contrail_cassandra_server_list__
REDIS_SERVER=$__contrail_redis_server__
REDIS_SERVER_PORT=$__contrail_redis_server_port__
DISCOVERY=$__contrail_discovery_ip__
HOST_IP=$__contrail_host_ip__
LISTEN_PORT=$__contrail_listen_port__
HTTP_SERVER_PORT=$__contrail_http_server_port__
LOG_FILE=$__contrail_log_file__
LOG_LOCAL=$__contrail_log_local__
LOG_LEVEL=$__contrail_log_level__
""")

qe_param_template = string.Template("""
CASSANDRA_SERVER_LIST=$__contrail_cassandra_server_list__
REDIS_SERVER=$__contrail_redis_server__
REDIS_SERVER_PORT=$__contrail_redis_server_port__
DISCOVERY=$__contrail_discovery_ip__
COLLECTORS=$__contrail_collectors__
LISTEN_PORT=$__contrail_listen_port__
HTTP_SERVER_PORT=$__contrail_http_server_port__
LOG_FILE=$__contrail_log_file__
LOG_LOCAL=$__contrail_log_local__
LOG_LEVEL=$__contrail_log_level__
""")

opserver_param_template = string.Template("""
REDIS_SERVER=$__contrail_redis_server__
REDIS_SERVER_PORT=$__contrail_redis_server_port__
REDIS_QUERY_PORT=$__contrail_redis_query_port__
HOST_IP=$__contrail_host_ip__
COLLECTORS=$__contrail_collectors__
HTTP_SERVER_PORT=$__contrail_http_server_port__
REST_API_PORT=$__contrail_rest_api_port__
LOG_FILE=$__contrail_log_file__
LOG_LOCAL=$__contrail_log_local__
LOG_LEVEL=$__contrail_log_level__
DISCOVERY=$__contrail_discovery_ip__
""")

vnc_api_lib_ini_template = string.Template("""
[global]
;WEB_SERVER = 127.0.0.1
;WEB_PORT = 9696  ; connection through quantum plugin

WEB_SERVER = 127.0.0.1
WEB_PORT = 8082 ; connection to api-server directly
BASE_URL = /
;BASE_URL = /tenants/infra ; common-prefix for all URLs

; Authentication settings (optional)
[auth]
AUTHN_TYPE = keystone
AUTHN_SERVER=$__contrail_openstack_ip__
AUTHN_PORT = 35357
AUTHN_URL = /v2.0/tokens
""")

agent_param_template = string.Template("""
LOG=/var/log/contrail.log
CONFIG=/etc/contrail/vnswad.conf
prog=/usr/bin/vnswad
kmod=vrouter/vrouter.ko
pname=vnswad
LIBDIR=/usr/lib64
VHOST_CFG=/etc/sysconfig/network-scripts/ifcfg-vhost0
VROUTER_LOGFILE=--DEFAULT.log_file=/var/log/vrouter.log
COLLECTOR=$__contrail_collector__
$__contrail_dev__
""")

vnswad_conf_template = string.Template("""
#
# Vnswad configuration options
#

[COLLECTOR]
# IP address and port to be used to connect to collector. If IP is not configured,
# value provided by discovery service will be used. (Optional)
port=$__contrail_collector_port__
server=$__contrail_collector_ip__

[CONTROL-NODE]
# IP address to be used to connect to control-node. Maximum of 2 IP addresses 
# (separated by a space) can be provided. If no IP is configured then the
# value provided by discovery service will be used. (Optional)
server=$__contrail_control_ip__

[DEFAULT]
# Everything in this section is optional

# Enable/disable debug logging. Possible values are 0 (disable) and 1 (enable)
# debug=0

# Aging time for flow-records in seconds
# flow_cache_timeout=0

# Hostname of compute-node. If this is not configured value from `hostname`
# will be taken
# hostname=

# Http server port for inspecting vnswad state (useful for debugging)
# http_server_port=8085

# Category for logging. Default value is '*'
# log_category=

# Local log file name
# log_file=/var/log/contrail/vrouter.log

# Log severity levels. Possible values are SYS_EMERG, SYS_ALERT, SYS_CRIT, 
# SYS_ERR, SYS_WARN, SYS_NOTICE, SYS_INFO and SYS_DEBUG. Default is SYS_DEBUG
# log_level=SYS_DEBUG

# Enable/Disable local file logging. Possible values are 0 (disable) and 1 (enable)
# log_local=0

# Encapsulation type for tunnel. Possible values are MPLSoGRE, MPLSoUDP, VXLAN
# tunnel_type=

[DISCOVERY]
# If COLLECTOR and/or CONTROL-NODE and/or DNS is not specified this section is 
# mandatory. Else this section is optional

# IP address of discovery server
# server=x.x.x.x

# Number of control-nodes info to be provided by Discovery service. Possible
# values are 1 and 2
# max_control_nodes=

[DNS]
# IP address to be used to connect to dns-node. Maximum of 2 IP addresses 
# (separated by a space) can be provided. If no IP is configured then the
# value provided by discovery service will be used. (Optional)
# server=10.0.0.1 10.0.0.2

[HYPERVISOR]
# Everything in this section is optional

# Hypervisor type. Possible values are kvm, xen and vmware
# type=kvm

# Link-local IP address and prefix in ip/prefix_len format (for xen)
# xen_ll_ip=

# Link-local interface name when hypervisor type is Xen
# xen_ll_interface=

# Physical interface name when hypervisor type is vmware
# vmware_physical_interface=

[FLOWS]
# Everything in this section is optional

# Maximum flows allowed per VM (given as % of maximum system flows)
# max_vm_flows=100
# Maximum number of link-local flows allowed across all VMs
# max_system_linklocal_flows=4096
# Maximum number of link-local flows allowed per VM
# max_vm_linklocal_flows=1024

[METADATA]
# Shared secret for metadata proxy service (Optional)
# metadata_proxy_secret=contrail

[NETWORKS]
# control-channel IP address used by WEB-UI to connect to vnswad to fetch
# required information (Optional)
control_network_ip=$__contrail_control_ip__

[VIRTUAL-HOST-INTERFACE]
# Everything in this section is mandatory

# name of virtual host interface
name=vhost0

# IP address and prefix in ip/prefix_len format
ip=$__contrail_box_ip__

# Gateway IP address for virtual host
gateway=$__contrail_gateway__

# Physical interface name to which virtual host interface maps to
physical_interface=$__contrail_intf__

# We can have multiple gateway sections with different indices in the 
# following format
[GATEWAY-0]
# Name of the routing_instance for which the gateway is being configured
# routing_instance=default-domain:admin:public:public

# Gateway interface name
# interface=vgw

# Virtual network ip blocks for which gateway service is required. Each IP
# block is represented as ip/prefix. Multiple IP blocks are represented by 
# separating each with a space
# ip_blocks=1.1.1.1/24

[GATEWAY-1]
# Name of the routing_instance for which the gateway is being configured
# routing_instance=default-domain:admin:public1:public1

# Gateway interface name
# interface=vgw1

# Virtual network ip blocks for which gateway service is required. Each IP
# block is represented as ip/prefix. Multiple IP blocks are represented by 
# separating each with a space
# ip_blocks=2.2.1.0/24 2.2.2.0/24

# Routes to be exported in routing_instance. Each route is represented as
# ip/prefix. Multiple routes are represented by separating each with a space
# routes=10.10.10.1/24 11.11.11.1/24
""")

vnswad_vgw_conf_template = string.Template("""
#
# Vnswad configuration options
#

[COLLECTOR]
# IP address and port to be used to connect to collector. If IP is not configured,
# value provided by discovery service will be used. (Optional)
# port=8086
# server=

[CONTROL-NODE]
# IP address to be used to connect to control-node. Maximum of 2 IP addresses 
# (separated by a space) can be provided. If no IP is configured then the
# value provided by discovery service will be used. (Optional)
server=$__contrail_control_ip__

[DEFAULT]
# Everything in this section is optional

# Enable/disable debug logging. Possible values are 0 (disable) and 1 (enable)
# debug=0

# Aging time for flow-records in seconds
# flow_cache_timeout=0

# Hostname of compute-node. If this is not configured value from `hostname`
# will be taken
# hostname=

# Http server port for inspecting vnswad state (useful for debugging)
# http_server_port=8085

# Category for logging. Default value is '*'
# log_category=

# Local log file name
# log_file=/var/log/contrail/vrouter.log

# Log severity levels. Possible values are SYS_EMERG, SYS_ALERT, SYS_CRIT, 
# SYS_ERR, SYS_WARN, SYS_NOTICE, SYS_INFO and SYS_DEBUG. Default is SYS_DEBUG
# log_level=SYS_DEBUG

# Enable/Disable local file logging. Possible values are 0 (disable) and 1 (enable)
# log_local=0

# Encapsulation type for tunnel. Possible values are MPLSoGRE, MPLSoUDP, VXLAN
# tunnel_type=

[DISCOVERY]
# If COLLECTOR and/or CONTROL-NODE and/or DNS is not specified this section is 
# mandatory. Else this section is optional

# IP address of discovery server
# server=x.x.x.x

# Number of control-nodes info to be provided by Discovery service. Possible
# values are 1 and 2
# max_control_nodes=

[DNS]
# IP address to be used to connect to dns-node. Maximum of 2 IP addresses 
# (separated by a space) can be provided. If no IP is configured then the
# value provided by discovery service will be used. (Optional)
# server=10.0.0.1 10.0.0.2

[HYPERVISOR]
# Everything in this section is optional

# Hypervisor type. Possible values are kvm, xen and vmware
# type=kvm

# Link-local IP address and prefix in ip/prefix_len format (for xen)
# xen_ll_ip=

# Link-local interface name when hypervisor type is Xen
# xen_ll_interface=

# Physical interface name when hypervisor type is vmware
# vmware_physical_interface=

[FLOWS]
# Everything in this section is optional

# Maximum flows allowed per VM (given as % of maximum system flows)
# max_vm_flows=100
# Maximum number of link-local flows allowed across all VMs
# max_system_linklocal_flows=4096
# Maximum number of link-local flows allowed per VM
# max_vm_linklocal_flows=1024

[METADATA]
# Shared secret for metadata proxy service (Optional)
# metadata_proxy_secret=contrail

[NETWORKS]
# control-channel IP address used by WEB-UI to connect to vnswad to fetch
# required information (Optional)
control_network_ip=$__contrail_control_ip__

[VIRTUAL-HOST-INTERFACE]
# Everything in this section is mandatory

# name of virtual host interface
name=vhost0

# IP address and prefix in ip/prefix_len format
ip=$__contrail_box_ip__

# Gateway IP address for virtual host
gateway=$__contrail_gateway__

# Physical interface name to which virtual host interface maps to
physical_interface=$__contrail_intf__

# We can have multiple gateway sections with different indices in the 
# following format
[GATEWAY-0]
# Name of the routing_instance for which the gateway is being configured
routing_instance=$__contrail_vgw_public_network__

# Gateway interface name
interface=$__contrail_vgw_interface__

# Virtual network ip blocks for which gateway service is required. Each IP
# block is represented as ip/prefix. Multiple IP blocks are represented by 
# separating each with a space
ip_blocks=$__contrail_vgw_public_subnet__

[GATEWAY-1]
# Name of the routing_instance for which the gateway is being configured
# routing_instance=default-domain:admin:public1:public1

# Gateway interface name
# interface=vgw1

# Virtual network ip blocks for which gateway service is required. Each IP
# block is represented as ip/prefix. Multiple IP blocks are represented by 
# separating each with a space
# ip_blocks=2.2.1.0/24 2.2.2.0/24

# Routes to be exported in routing_instance. Each route is represented as
# ip/prefix. Multiple routes are represented by separating each with a space
# routes=10.10.10.1/24 11.11.11.1/24
""")

ifconfig_vhost0_template = string.Template("""
#Contrail vhost0
DEVICE=vhost0
ONBOOT=yes
BOOTPROTO=none
IPV6INIT=no
USERCTL=yes
IPADDR=$__contrail_ipaddr__
NETMASK=$__contrail_netmask__
NM_CONTROLLED=no
#NETWORK MANAGER BUG WORKAROUND
SUBCHANNELS=1,2,3
$__contrail_gateway__
$__contrail_dns__
$__contrail_domain__
$__contrail_mtu__
""")

contrail_plugin_template = string.Template("""
[APISERVER]
api_server_ip=$__api_server_ip__
api_server_port=$__api_server_port__
multi_tenancy=$__multitenancy__

[KEYSTONE]
admin_user=$__contrail_admin_user__
admin_password=$__contrail_admin_password__
admin_tenant_name=$__contrail_admin_tenant_name__
""")

openstackrc_template = string.Template("""
export OS_USERNAME=$__contrail_admin_user__
export OS_PASSWORD=$__contrail_admin_password__
export OS_TENANT_NAME=$__contrail_admin_tenant_name__
export OS_AUTH_URL=http://$__contrail_keystone_ip__:5000/v2.0/
export OS_NO_CACHE=1
""")

