# nebula2nt

> nebula导出数据转为nt数据

## 数据预处理

将导出的nubula数据分为点文件node.txt和edge.txt，放入input文件夹中

* ./input/node.txt数据示例

> match (v) return v，id(v) as vid 

```bash
{"vid":"-1003415155","v":{"jstp_hnu.type":"人物","jstp_hnu.name":"张三","jstp_hnu.id":"56465"}}
{"vid":"-1003461111","v":{"jstp_hnu.type":"人物","jstp_hnu.name":"赵六","jstp_hnu.id":"56188"}}
{"vid":"-1003461122","v":{"jstp_hnu.type":"人物","jstp_hnu.name":"花生","jstp_hnu.id":"56199"}}
```

* ./input/edge.txt数据示例

> match (v)-[e]->(v2) return id(v) as v1,type(e) as type,id(v2) as v2

```bash
{"v1":"44","type":"母亲","v2":"43"}
{"v1":"-100358735","type":"推荐模块验证关系","v2":"-100358723"}
{"v1":"-100358735","type":"推荐模块验证关系","v2":"-100358843"}
```

## 使用

```bash
# linux环境
python3 transfer_node.py
python3 transfer_edge.py
```

## 输出结果

```bash
./output/    # 结果输出文件夹
./output/all.nt    # 存储所有的点和边数据
./output/node.nt   # 存储所有的点数据
./output/edge.nt   # 存储所有的边数据
```

> note: 属性type、属性name和属性id转化为字面值("")

## 数据导入gStore(命令行)

```bash
# all.nt可以放在gstore目录下，或者使用绝对路径
bin/gbuild -db test -f all.nt
```

## gstore查询执行
### 查询执行
```bash
# 查询语句放在test.sql文件中，test.sql可以放在gstore目录下或者使用绝对路径
bin/gquery -db test -q test.sql
```
### 查询语句示例
```sparql
# 查询所有实体（真实id）
select distinct ?s where 
{ 
	?s ?p ?o . 
}

# 查询实体的属性（以真实id为-1003415155的点为例）
SELECT DISTINCT ?property
WHERE {
  <-1003415155> ?predicate ?property .
  FILTER(isLiteral(?property))
}

# 查询实体的邻居实体（以真实id为-1003415155的点为例）
SELECT DISTINCT ?neighbor
WHERE {
  <-1003415155> ?predicate ?neighbor .
  FILTER(isURI(?neighbor))
}

# 查询所有的边类型
SELECT DISTINCT ?predicate
WHERE {
  ?subject ?predicate ?object .
}
```