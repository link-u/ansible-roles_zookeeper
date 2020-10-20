# ZooKeeper

![ansible ci](https://github.com/link-u/ansible-roles_zookeeper/workflows/ansible%20ci/badge.svg)

## 概要

ZooKeeper をインストールする ansible role

## 動作確認バージョン

- Ubuntu 18.04 (bionic)
- Ubuntu 20.04 (focal)
- ansible >= 2.8
- Jinja2 2.10.3

## 使い方 (ansible)

### Role variables

```yaml
### インストール設定 ###############################################################################
## 基本設定
zookeeper_install_flag: True          # インストールフラグ


### zookeeper の設定 ##############################################################################
## 基本設定
zookeeper_tickTime: "2000"
zookeeper_dataDir: "/var/lib/zookeeper"
zookeeper_clientPort: "2181"
zookeeper_initLimit: "5"
zookeeper_syncLimit: "2"

## クラスタに関する設定
zookeeper_server_ips: >-
  {{ (group_names | map('extract', groups) | list)[0] |
      map('extract', hostvars, 'local_ipv4') | list }}
```

### Example playbook
```yaml
- hosts:
    - servers
  roles:
    - { role: zookeeper, tags: [ "zookeeper" ] }
```
