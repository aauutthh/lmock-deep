
[lmock](https://github.com/wangyongfeng5/lmock)
[效能优化实践：C/C++单元测试万能插桩工具](https://zhuanlan.zhihu.com/p/379605663?utm_source=ZHShareTargetIDMore&utm_medium=social&utm_oi=30090834477056)
作者: 腾讯技术 mannywang

缺点:
1. 多个测试无法并行, 缺少context. （这可以通过get_contex()的hook函数由用户自定义, 库提供create_context）
2. mock(&global, &fake_global), 函数内部缺少重复mock检查， 多次调用就无法进行恢复了。

优化点:
1. 跳转到固定的函数, 并由函数计算出应跳转到的具体函数, 方便统一管理, 不需要反复修改函数入口
2. 函数跳转可设开关，reset时关闭所有开关
3. 跳转到固定函数后如何识别原函数入口? 栈?

