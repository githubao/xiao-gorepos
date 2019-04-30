# xiao-gorepos
500+ golang open source repos

[TOC]
### TODO
- 105th of 1599
- 116 to go with 500

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

#### web框架和路由
1. 高性能极简的web框架: [labstack/echo](github.com/labstack/echo)
1. 高性能重量web框架: [astaxie/beego](github.com/astaxie/beego)
1. 最常用的web框架: [gin-gonic/gin](github.com/gin-gonic/gin)
1. 高生产率全栈的web框架: [revel/revel](github.com/revel/revel)
1. 轻量可组合的web框架: [go-chi/chi](github.com/go-chi/chi)
1. 最快的web框架: [kataras/iris](github.com/kataras/iris)
1. 更快的web框架: [valyala/fasthttp](github.com/valyala/fasthttp)
1. 高性能web框架: [julienschmidt/httprouter](github.com/julienschmidt/httprouter)

#### 开发和构建
1. rpc框架: [go-kit/kit](github.com/go-kit/kit)
1. 常见中间件: [urfave/negroni](github.com/urfave/negroni)
1. 微服务工具集: [micro/micro](github.com/micro/micro)
1. 更快的多语言rpc框架: [smallnest/rpcx](github.com/smallnest/rpcx)

#### 鉴权
1. httpauth: [goji/httpauth](github.com/goji/httpauth)
1. authboss: [volatiletech/authboss](github.com/volatiletech/authboss)

#### 序列化
1. rpc序列化: [ugorji/go](github.com/ugorji/go)
1. grpc和json数据转化: [grpc-ecosystem/grpc-gateway](github.com/grpc-ecosystem/grpc-gateway)

#### 服务治理
1. 限速: [juju/ratelimit](github.com/juju/ratelimit)
1. 断路器: [rubyist/circuitbreaker](github.com/rubyist/circuitbreaker)
1. 重试: [kamilsk/retry](github.com/kamilsk/retry)
1. 断路器: [afex/hystrix-go](github.com/afex/hystrix-go)
1. 断路器: [netflix/hystrix](github.com/netflix/hystrix)

#### 爬虫
1. 爬虫框架: [gocolly/colly](github.com/gocolly/colly)
1. jquery解析器: [puerkitobio/goquery](github.com/puerkitobio/goquery)

#### 网络聊天
1. websocket网络聊天: [olahol/melody](github.com/olahol/melody)
1. 实时聊天: [centrifugal/centrifugo](github.com/centrifugal/centrifugo)

### 存储

#### 数据库驱动
1. mysql: [go-sql-driver/mysql](github.com/go-sql-driver/mysql)
1. mymysql: [ziutek/mymysql](github.com/ziutek/mymysql)
1. postgresql: [lib/pq](github.com/lib/pq)
1. sqlite3: [mattn/go-sqlite3](github.com/mattn/go-sqlite3)

#### 分布式db
1. 水平扩展sql: [vitessio/vitess](github.com/vitessio/vitess)
1. 分布式mysql: [pingcap/tidb](github.com/pingcap/tidb)
1. 分布式可扩展sql: [cockroachdb/cockroach](github.com/cockroachdb/cockroach)

#### 数据库工具
1. go-orm: [jinzhu/gorm](github.com/jinzhu/gorm)
1. xorm: [go-xorm/xorm](github.com/go-xorm/xorm)
1. sql工具集: [jmoiron/sqlx](github.com/jmoiron/sqlx)
1. 命令行sql: [xo/usql](github.com/xo/usql)

#### 内存数据库
1. 内存存储: [muesli/cache2go](github.com/muesli/cache2go)
1. redis: [go-redis/redis](github.com/go-redis/redis)
1. kv存储: [boltdb/bolt](github.com/boltdb/bolt)
1. kv数据库: [dgraph-io/badger](github.com/dgraph-io/badger)
1. 可过期的内存缓存: [bluele/gcache](github.com/bluele/gcache)

#### nosql
1. elastic: [olivere/elastic](github.com/olivere/elastic)
1. 图数据库: [dgraph-io/dgraph](github.com/dgraph-io/dgraph)
1. 图数据库: [cayleygraph/cayley](github.com/cayleygraph/cayley)
1. 文件存储: [mbdavid/litedb](github.com/mbdavid/litedb)

#### graphql
1. graphql: [graphql-go/graphql](github.com/graphql-go/graphql)
1. 构建graphsq服务: [99designs/gqlgen](github.com/99designs/gqlgen)

#### 消息格式
1. proto: [gogo/protobuf](github.com/gogo/protobuf)
1. proto: [golang/protobuf](github.com/golang/protobuf)
1. msgp: [tinylib/msgp](github.com/tinylib/msgp)

#### json
1. 简单json解析: [bitly/go-simplejson](github.com/bitly/go-simplejson)
1. 最快的json解析库: [json-iterator/go](github.com/json-iterator/go)
1. 可以解析路径的json: [tidwall/gjson](github.com/tidwall/gjson)

#### 压缩
1. snappy压缩格式: [golang/snappy](github.com/golang/snappy)
1. snappy-stream: [mreiferson/go-snappystream](github.com/mreiferson/go-snappystream)
1. zstd: [datadog/zstd](github.com/datadog/zstd)

#### 消息队列
1. nsq客户端: [nsqio/go-nsq](github.com/nsqio/go-nsq)
1. kafka: [shopify/sarama](github.com/shopify/sarama)
1. nsq-server: [nsqio/nsq](github.com/nsqio/nsq)
1. rabbitmq: [streadway/amqp](github.com/streadway/amqp)
1. activemq: [go-stomp/stomp](github.com/go-stomp/stomp)

#### 大数据
1. hdfs客户端: [colinmarc/hdfs](github.com/colinmarc/hdfs)

#### 分布式存储
1. etcd: [etcd-io/etcd](github.com/etcd-io/etcd)

### 工具

#### utils
1. 工具集: [shomali11/util](github.com/shomali11/util)
1. 工具集: [juju/utils](github.com/juju/utils)
1. 工具集: [coreos/pkg](github.com/coreos/pkg)

#### 语言工具
1. 并发工具: [modern-go/concurrent](github.com/modern-go/concurrent)
1. 错误堆栈: [pkg/errors](github.com/pkg/errors)
1. 性能更好的反射: [modern-go/reflect2](github.com/modern-go/reflect2)
1. gls: [modern-go/gls](github.com/modern-go/gls)

### 集合
1. set集合: [deckarep/golang-set](github.com/deckarep/golang-set)
1. 并发安全的map: [streamrail/concurrent-map](github.com/streamrail/concurrent-map)
1. 数据结构和集合: [go-datastructures](github.com/Workiva/go-datastructures)
1. 数据结构和集合: [emirpasic/gods](github.com/emirpasic/gods)

### 设计模式
1. golang常见的设计模式: [tmrts/go-patterns](github.com/tmrts/go-patterns)

### 函数式编程
1. 流式计算: [chrislusf/glow](github.com/chrislusf/glow)
1. 函数式编程: [ahl5esoft/golang-underscore](github.com/ahl5esoft/golang-underscore)

### 文本相关
1. 命令行模糊搜索: [junegunn/fzf](github.com/junegunn/fzf)
1. 交互式文本过滤: [peco/peco](github.com/peco/peco)
1. tag验证: [go-playground/validator](github.com/go-playground/validator)

#### 算法
1. 时间最久淘汰: [juju/lru](github.com/juju/lru)
1. set和deque: [juju/collections](github.com/juju/collections)
1. bitset: [willf/bitset](github.com/willf/bitset)
1. 布隆过滤器: [tylertreat/boomfilters](github.com/tylertreat/boomfilters)
1. deque: [gammazero/deque](github.com/gammazero/deque)
1. 内存缓存: [golang/groupcache](github.com/golang/groupcache)

#### 配置文件
1. 处理配置信息: [spf13/viper](github.com/spf13/viper)
1. yaml解析: [go-yaml/yaml](github.com/go-yaml/yaml)
1. toml解析: [pelletier/toml](github.com/pelletier/go-toml)
1. hcl解析: [hashicorp/hcl](github.com/hashicorp/hcl)
1. xml/html解析: [antchfx/xquery](github.com/antchfx/xquery)

#### uuid
1. go-uuid: [satori/go.uuid](github.com/satori/go.uuid)
1. google-uuid: [google/uuid](github.com/google/uuid)

#### http client
1. http请求: [pkg/requests](github.com/pkg/requests)
1. http请求: [mozillazg/request](github.com/mozillazg/request)
1. 流式http请求: [smallnest/goreq](github.com/smallnest/goreq)
1. 模拟py的requests: [levigross/grequests](github.com/levigross/grequests)
1. 全武装的http: [h2non/gentleman](github.com/h2non/gentleman)
1. 加强的http请求: [heimdall](github.com/gojektech/heimdall)

#### 学习
1. golang书籍: [dariubs/gobooks](github.com/dariubs/gobooks)
1. go工程结构: [golang-standards/project-layout](github.com/golang-standards/project-layout)

#### 搜索
1. 文件索引: [blevesearch/bleve](github.com/blevesearch/bleve)
1. 分布式搜索: [go-ego/riot](github.com/go-ego/riot)
1. 机器学习: [sjwhitworth/golearn](github.com/sjwhitworth/golearn)
1. solr客户端: [sendgrid/go-solr](github.com/sendgrid/go-solr)

#### 加密
1. web令牌: [dgrijalva/jwt-go](github.com/dgrijalva/jwt-go)

#### 命令行界面 
1. 命令行cli: [spf13/cobra](github.com/spf13/cobra)
1. 命令行cli: [urfave/cli](github.com/urfave/cli)

#### 日志
1. logrus: [sirupsen/logrus](github.com/sirupsen/logrus)
1. 高性能日志: [uber-go/zap](github.com/uber-go/zap)
1. 可视化错误日志监控sentry: [getsentry/raven-go](github.com/getsentry/raven-go)

#### debug
1. 打印: [davecgh/go-spew](github.com/davecgh/go-spew)
1. 打印: [luci/go-render](github.com/luci/go-render)
1. 优美打印: [go-ffmt/ffmt](github.com/go-ffmt/ffmt)
1. 调试工具: [derekparker/delve](github.com/derekparker/delve)

#### 监控
1. 分布式追踪: [opentracing/opentracing-go](github.com/opentracing/opentracing-go)
1. 分布式追踪: [jaegertracing/jaeger](github.com/jaegertracing/jaeger)
1. 打点: [rcrowley/go-metrics](github.com/rcrowley/go-metrics)
1. 时序数据库: [influxdata/influxdb](github.com/influxdata/influxdb)
1. flux查询语言: [influxdata/flux](github.com/influxdata/flux)
1. 监控和时序数据库: [prometheus/prometheus](github.com/prometheus/prometheus)

#### 测试
1. 测试工具和bdd: [onsi/ginkgo](github.com/onsi/ginkgo)
1. 测试工具集: [stretchr/testify](github.com/stretchr/testify)
1. mock数据: [golang/mock](github.com/golang/mock)
1. 行为驱动开发测试(bdd): [data-dog/godog](github.com/data-dog/godog)

#### 依赖管理
1. dep: [golang/dep](github.com/golang/dep)
1. govendor: [kardianos/govendor](github.com/kardianos/govendor)
1. glide: [masterminds/glide](github.com/masterminds/glide)

#### Git相关
1. 更好用的git: [github/hub](github.com/github/hub)
1. git管理系统: [gogs/gogs](github.com/gogs/gogs)

#### 未归类
1. 静态网站生成器: [gohugoio/hugo](github.com/gohugoio/hugo)
1. 二维码: [skip2/go-qrcode](github.com/skip2/go-qrcode)
1. 文件备份: [restic/restic](github.com/restic/restic)
