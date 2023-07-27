# Selected Features
Some of the most **relevant AND recommended** features for network intrusion detection are:

| Feature | Description |
| --- | --- |
| Duration | Length of time duration of the connection |
| Src_bytes | Number of data bytes transferred from source to destination in single connection |
| Dst_bytes | Number of data bytes transferred from destination to source in single connection |
| Count | Number of connections to the same destination host as the current connection in the past two seconds |
| Srv_count | Number of connections to the same service (port number) as the current connection in the past two seconds |
| Same_srv_rate | The percentage of connections that were to the same service, among the connections aggregated in count (23) |
| Diff_srv_rate | The percentage of connections that were to different services, among the connections aggregated in count (23) |
| Dst_host_count | Number of connections having the same destination host IP address |
| Dst_host_srv_count | Number of connections having the same port number |
| Dst_host_same_srv_rate | The percentage of connections that were to the same service, among the connections aggregated in dst_host_count (32) |
| Dst_host_diff_srv_rate | The percentage of connections that were to different services, among the connections aggregated in dst_host_count (32) |
| Dst_host_same_src_port_rate | The percentage of connections that were to the same source port, among the connections aggregated in dst_host_srv_count (33) |
| Dst_host_serror_rate | The percentage of connectionsthat have activated the flag (4) s0, s1, s2 or s3, among the connections aggregated in dst_host_count (32) |

