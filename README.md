# xiao-gorepos
500+ golang open source repos

[TOC]
### REF
- [awemesome-go](https://github.com/avelino/awesome-go)
- [awemesome-go-cn](https://github.com/jobbole/awesome-go-cn)
- 先"ag github.com ./", 然后运行github.py统计


### web服务

#### 容器
1. docker: [Moby](github.com/moby/moby)
1. 容器管理调度: [kubernetes](github.com/kubernetes/kubernetes)
1. 容器核心组件: [containerd](github.com/containerd/containerd)

#### rpc
1. grpc: [grpc-go](github.com/grpc/grpc-go)
1. thrift: [thrift](github.com/apache/thrift)
1. thrift: [go-thrift](github.com/samuel/go-thrift)

#### web框架
1. 最常用的web框架: [gin](github.com/gin-gonic/gin)
1. 更快的web框架: [fasthttp](github.com/valyala/fasthttp)
1. 常见的web框架: [echo](github.com/labstack/echo)

#### 构建
1. kit: [kit](github.com/go-kit/kit)

#### 鉴权
1. httpauth: [httpauth](github.com/Goji/httpauth)

#### 序列化
1. rpc序列化: [go](github.com/ugorji/go)

#### 服务治理
1. 限速: [ratelimit](github.com/juju/ratelimit)
1. 断路器: [circuitbreaker](github.com/rubyist/circuitbreaker)
1. 重试: [retry](github.com/kamilsk/retry)
1. 断路器: [hystrix-go](github.com/afex/hystrix-go)
1. 断路器: [hystrix](github.com/netflix/hystrix)

### 存储

#### 数据库
1. mysql: [mysql](github.com/go-sql-driver/mysql)
1. mymysql: [mymysql](github.com/ziutek/mymysql)
1. go-orm: [gorm](github.com/jinzhu/gorm)
1. postgresql: [pq](github.com/lib/pq)
1. sqlite3: [go-sqlite3](github.com/mattn/go-sqlite3)
1. 分布式mysql: [tidb](github.com/pingcap/tidb)

#### nosql
1. redis: [redis](github.com/go-redis/redis)
1. graphql: [graphql](github.com/graphql-go/graphql)
1. elastic: [elastic](github.com/olivere/elastic)
1. kv存储: [bolt](github.com/boltdb/bolt)
1. 内存存储: [cache2go](github.com/muesli/cache2go)

#### 消息格式
1. proto: [protobuf](github.com/gogo/protobuf)
1. proto: [protobuf](github.com/golang/protobuf)
1. msgp: [msgp](github.com/tinylib/msgp)

#### json
1. json解析: [go-simplejson](github.com/bitly/go-simplejson)
1. 最快的json解析库: [go](github.com/json-iterator/go)

#### 压缩
1. snappy压缩格式: [snappy](github.com/golang/snappy)
1. snappy-stream: [go-snappystream](github.com/mreiferson/go-snappystream)
1. zstd: [zstd](github.com/datadog/zstd)

#### 消息队列
1. nsq客户端: [go-nsq](github.com/nsqio/go-nsq)
1. kafka: [sarama](github.com/Shopify/sarama)
1. nsq-server: [nsq](github.com/nsqio/nsq)

#### 大数据
1. hdfs客户端: [hdfs](github.com/colinmarc/hdfs)

#### 分布式存储
1. etcd: [etcd](github.com/etcd-io/etcd)

### 工具

#### 工具合集
1. 工具集: [util](github.com/shomali11/util)
1. 工具集: [utils](github.com/juju/utils)
1. 工具集: [pkg](github.com/coreos/pkg)

#### 更好用的工具
1. set集合: [golang-set](github.com/deckarep/golang-set)
1. 并发安全的map: [concurrent-map](github.com/streamrail/concurrent-map)
1. 错误堆栈: [errors](github.com/pkg/errors)
1. 性能更好的反射: [reflect2](github.com/modern-go/reflect2)
1. 并发工具: [concurrent](github.com/modern-go/concurrent)
1. gls: [gls](github.com/modern-go/gls)

#### 算法
1. 时间最久淘汰: [lru](github.com/juju/lru)
1. set和deque: [collections](github.com/juju/collections)
1. bitset: [bitset](github.com/willf/bitset)
1. 布隆过滤器: [boomfilters](github.com/tylertreat/boomfilters)

#### 配置文件
1. yaml解析: [yaml](github.com/go-yaml/yaml)
1. 处理配置信息: [viper](github.com/spf13/viper)
1. toml解析: [toml](github.com/pelletier/go-toml)
1. hcl解析: [hcl](github.com/hashicorp/hcl)

#### uuid
1. go-uuid: [go.uuid](github.com/satori/go.uuid)
1. google-uuid: [uuid](github.com/google/uuid)

#### debug
1. 打印: [go-spew](github.com/davecgh/go-spew)
1. 打印: [go-render](github.com/luci/go-render)

#### http
1. http请求: [requests](github.com/pkg/requests)
1. http请求: [request](github.com/mozillazg/request)
1. 流式http请求: [goreq](github.com/smallnest/goreq)
1. requests: [grequests](github.com/levigross/grequests)

#### CLI
1. 命令行cli: [cobra](github.com/spf13/cobra)
1. 命令行cli: [cli](github.com/urfave/cli)

#### 监控
1. 分布式追踪: [opentracing-go](github.com/opentracing/opentracing-go)
1. 打点: [go-metrics](github.com/rcrowley/go-metrics)
1. 时序数据库: [influxdb](github.com/influxdata/influxdb)
1. flux查询语言: [flux](github.com/influxdata/flux)

#### 测试
1. 行为驱动开发测试: [ginkgo](github.com/onsi/ginkgo)

#### 依赖管理
1. dep: [dep](github.com/golang/dep)
1. govendor: [govendor](github.com/kardianos/govendor)
1. glide: [glide](github.com/Masterminds/glide)

### 未归类

1. 静态网站生成器: [hugo](github.com/gohugoio/hugo)
1. git管理系统: [gogs](github.com/gogs/gogs)
1. 调试工具: [delve](github.com/derekparker/delve)
1. 二维码: [go-qrcode](github.com/skip2/go-qrcode)

