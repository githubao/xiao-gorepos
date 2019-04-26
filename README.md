# xiao-gorepos
500+ golang open source repos

[TOC]
### REF
- [avelino/awemesome-go](https://github.com/avelino/awesome-go)
- [jobbole/awemesome-go-cn](https://github.com/jobbole/awesome-go-cn)
- ag then count


### web服务

#### 容器
1. docker: [moby/moby](github.com/moby/moby)
1. 容器管理调度: [kubernetes/kubernetes](github.com/kubernetes/kubernetes)
1. 容器核心组件: [containerd/containerd](github.com/containerd/containerd)

#### rpc
1. grpc: [grpc/grpc-go](github.com/grpc/grpc-go)
1. thrift: [apache/thrift](github.com/apache/thrift)
1. thrift: [samuel/go-thrift](github.com/samuel/go-thrift)

#### web框架
1. 最常用的web框架: [gin-gonic/gin](github.com/gin-gonic/gin)
1. 更快的web框架: [valyala/fasthttp](github.com/valyala/fasthttp)
1. 常见的web框架: [labstack/echo](github.com/labstack/echo)

#### 构建
1. kit: [go-kit/kit](github.com/go-kit/kit)

#### 鉴权
1. httpauth: [goji/httpauth](github.com/goji/httpauth)

#### 序列化
1. rpc序列化: [ugorji/go](github.com/ugorji/go)

#### 服务治理
1. 限速: [juju/ratelimit](github.com/juju/ratelimit)
1. 断路器: [rubyist/circuitbreaker](github.com/rubyist/circuitbreaker)
1. 重试: [kamilsk/retry](github.com/kamilsk/retry)
1. 断路器: [afex/hystrix-go](github.com/afex/hystrix-go)
1. 断路器: [netflix/hystrix](github.com/netflix/hystrix)

### 存储

#### 数据库
1. mysql: [go-sql-driver/mysql](github.com/go-sql-driver/mysql)
1. mymysql: [ziutek/mymysql](github.com/ziutek/mymysql)
1. go-orm: [jinzhu/gorm](github.com/jinzhu/gorm)
1. postgresql: [lib/pq](github.com/lib/pq)
1. sqlite3: [mattn/go-sqlite3](github.com/mattn/go-sqlite3)
1. 分布式mysql: [pingcap/tidb](github.com/pingcap/tidb)

#### nosql
1. redis: [go-redis/redis](github.com/go-redis/redis)
1. graphql: [graphql-go/graphql](github.com/graphql-go/graphql)
1. elastic: [olivere/elastic](github.com/olivere/elastic)
1. kv存储: [boltdb/bolt](github.com/boltdb/bolt)
1. 内存存储: [muesli/cache2go](github.com/muesli/cache2go)

#### 消息格式
1. proto: [gogo/protobuf](github.com/gogo/protobuf)
1. proto: [golang/protobuf](github.com/golang/protobuf)
1. msgp: [tinylib/msgp](github.com/tinylib/msgp)

#### json
1. json解析: [bitly/go-simplejson](github.com/bitly/go-simplejson)
1. 最快的json解析库: [json-iterator/go](github.com/json-iterator/go)

#### 压缩
1. snappy压缩格式: [golang/snappy](github.com/golang/snappy)
1. snappy-stream: [mreiferson/go-snappystream](github.com/mreiferson/go-snappystream)
1. zstd: [datadog/zstd](github.com/datadog/zstd)

#### 消息队列
1. nsq客户端: [nsqio/go-nsq](github.com/nsqio/go-nsq)
1. kafka: [shopify/sarama](github.com/shopify/sarama)
1. nsq-server: [nsqio/nsq](github.com/nsqio/nsq)

#### 大数据
1. hdfs客户端: [colinmarc/hdfs](github.com/colinmarc/hdfs)

#### 分布式存储
1. etcd: [etcd-io/etcd](github.com/etcd-io/etcd)

### 工具

#### 工具合集
1. 工具集: [shomali11/util](github.com/shomali11/util)
1. 工具集: [juju/utils](github.com/juju/utils)
1. 工具集: [coreos/pkg](github.com/coreos/pkg)

#### 更好用的工具
1. set集合: [deckarep/golang-set](github.com/deckarep/golang-set)
1. 并发安全的map: [streamrail/concurrent-map](github.com/streamrail/concurrent-map)
1. 错误堆栈: [pkg/errors](github.com/pkg/errors)
1. 性能更好的反射: [modern-go/reflect2](github.com/modern-go/reflect2)
1. 并发工具: [modern-go/concurrent](github.com/modern-go/concurrent)
1. gls: [modern-go/gls](github.com/modern-go/gls)

#### 算法
1. 时间最久淘汰: [juju/lru](github.com/juju/lru)
1. set和deque: [juju/collections](github.com/juju/collections)
1. bitset: [willf/bitset](github.com/willf/bitset)
1. 布隆过滤器: [tylertreat/boomfilters](github.com/tylertreat/boomfilters)
1. deque: [gammazero/deque](github.com/gammazero/deque)

#### 配置文件
1. 处理配置信息: [spf13/viper](github.com/spf13/viper)
1. yaml解析: [go-yaml/yaml](github.com/go-yaml/yaml)
1. toml解析: [pelletier/toml](github.com/pelletier/go-toml)
1. hcl解析: [hashicorp/hcl](github.com/hashicorp/hcl)
1. xml/html解析: [antchfx/xquery](github.com/antchfx/xquery)

#### uuid
1. go-uuid: [satori/go.uuid](github.com/satori/go.uuid)
1. google-uuid: [google/uuid](github.com/google/uuid)

#### 日志
1. logrus: [sirupsen/logrus](github.com/sirupsen/logrus)

#### debug
1. 打印: [davecgh/go-spew](github.com/davecgh/go-spew)
1. 打印: [luci/go-render](github.com/luci/go-render)
1. 格式化打印: [go-ffmt/ffmt](github.com/go-ffmt/ffmt)

#### http
1. http请求: [pkg/requests](github.com/pkg/requests)
1. http请求: [mozillazg/request](github.com/mozillazg/request)
1. 流式http请求: [smallnest/goreq](github.com/smallnest/goreq)
1. requests: [levigross/grequests](github.com/levigross/grequests)

#### CLI
1. 命令行cli: [spf13/cobra](github.com/spf13/cobra)
1. 命令行cli: [urfave/cli](github.com/urfave/cli)

#### 监控
1. 分布式追踪: [opentracing/opentracing-go](github.com/opentracing/opentracing-go)
1. 打点: [rcrowley/go-metrics](github.com/rcrowley/go-metrics)
1. 时序数据库: [influxdata/influxdb](github.com/influxdata/influxdb)
1. flux查询语言: [influxdata/flux](github.com/influxdata/flux)

#### 测试
1. 行为驱动开发测试: [onsi/ginkgo](github.com/onsi/ginkgo)

#### 依赖管理
1. dep: [golang/dep](github.com/golang/dep)
1. govendor: [kardianos/govendor](github.com/kardianos/govendor)
1. glide: [masterminds/glide](github.com/masterminds/glide)

### 未归类

1. 静态网站生成器: [gohugoio/hugo](github.com/gohugoio/hugo)
1. git管理系统: [gogs/gogs](github.com/gogs/gogs)
1. 调试工具: [derekparker/delve](github.com/derekparker/delve)
1. 二维码: [skip2/go-qrcode](github.com/skip2/go-qrcode)

