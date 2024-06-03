<template>
  <div class="home">
    <transition name="fade" mode="out-in">

      <dv-border-box-10>
        <div class="naca">
          <div class="index-header" style="margin-top: 5px">
            <div>
              <dv-decoration-10 style="width: 450px; height: 1px; margin-bottom: 45px" />
              <dv-decoration-8 style="width: 180px; height: 50px" :color="['#568aea', '#000000']" />
              <div style="
                  width: 150px;
                  color: #eeecec;
                  font-size: 18px;
                  padding: 0 15px;
                  font-weight: bold;
                ">
                可视化化平台
              </div>
              <dv-decoration-8 :reverse="true" style="width: 180px; height: 50px" :color="['#568aea', '#000000']" />
              <dv-decoration-10 style="
                  width: 450px;
                  height: 1px;
                  transform: rotateY(180deg);
                  margin-bottom: 45px;
                " />
            </div>
            <dv-decoration-5 style="width: 10%; height: 20px" :color="['#568aea', '#000000']" />
          </div>

          <div class="index-content">
            <div class="left">
              <div class="col-1" style="">

                <dv-border-box-12 style="height: 300px; width: 490px">
                  <div class="title" style="margin-top: 5px">
                    历史记录
                  </div>
                  <div ref="firstMain" style="width: 100%; height: 105%"></div>
                </dv-border-box-12>

                <dv-border-box-12 style="height: 250px; width: 490px">
                  <div class="title" style="margin-top: 5px">
                    设备状态
                  </div>
                  <div ref="secondMain" style="width: 70%; height: 100%">
                    <template>
                      <el-tabs v-model="activeName" @tab-click="handleClick" style="margin-left: 50px;">
                        <el-tab-pane label="主控" name="first">主控</el-tab-pane>
                        <el-tab-pane label="时间校准" name="second">时间校准</el-tab-pane>
                        <el-tab-pane label="通道" name="third">通道</el-tab-pane>
                        <el-tab-pane label="告警" name="fourth">告警</el-tab-pane>
                      </el-tabs>
                    </template>
                  </div>
                </dv-border-box-12>



              </div>
            </div>

            <div class="cent">
              <div class="col-2" style="">

                <dv-border-box-12 style="height: 300px; width: 410px">
                  <div class="title" style="margin-top: 5px">
                    水文气象
                  </div>
                  <div ref="thirdMain" style="width: 100%; height: 100%"></div>
                </dv-border-box-12>

                <dv-border-box-12 style="height: 250px; width: 410px">
                  <div class="title" style="margin-top: 5px">
                    定位
                  </div>
                  <div ref="fourthMain" style="width: 93%; height: 83%; margin-left: 15px">
                    <template>
                      <div id="map" style="width: 100%; height: 100%"></div>
                    </template>
                  </div>
                </dv-border-box-12>

              </div>
            </div>

            <div class="right">
              <div class="col-3" style="">
                <dv-border-box-12 style="height: 330px; width: 540px">
                  <div class="title" style="margin-top: 5px">
                    监控视频
                  </div>
                  <div id="fifthMain" style="width: 63%; height: 90px">
                    <template>
                      <el-tabs v-model="activeName2" @tab-click="handleClick2" style="margin-left: 50px;">
                        <el-tab-pane label="视频1" name="first">视频1</el-tab-pane>
                        <el-tab-pane label="视频2" name="second">视频2</el-tab-pane>
                        <el-tab-pane label="视频3" name="third">视频3</el-tab-pane>
                        <el-tab-pane label="视频4" name="fourth">视频4</el-tab-pane>
                      </el-tabs>
                    </template>
                  </div>
                </dv-border-box-12>

                <dv-border-box-12 style="height: 220px; width: 540px">
                  <div class="title" style="margin-top: 5px">
                    附加功能
                  </div>
                  <div id="sixthMain"
                    style="display: grid; grid-template-columns: repeat(3, 1fr); width: 98%; height: 90%">
                    <div class="rounded-box"
                      style="display: flex; flex-direction: row; justify-content: flex-start; align-items: center;">
                      摄像头
                      <camera-icon style="margin-left: auto;" />
                    </div>
                    <div class="rounded-box"
                      style="display: flex; flex-direction: row; justify-content: flex-start; align-items: center;">
                      灯光
                      <light-icon style="margin-left: auto;" />
                    </div>
                    <div class="rounded-box"
                      style="display: flex; flex-direction: row; justify-content: flex-start; align-items: center;">
                      清洁
                      <brush-icon style="margin-left: auto;" />
                    </div>
                    <div class="rounded-box"
                      style="display: flex; flex-direction: row; justify-content: flex-start; align-items: center;">
                      回放
                      <loop-icon style="margin-left: auto;" />
                    </div>
                    <div class="rounded-box"
                      style="display: flex; flex-direction: row; justify-content: flex-start; align-items: center;">
                      同时播放
                      <split-screen-icon style="margin-left: auto;" />
                    </div>
                    <div class="rounded-box"
                      style="display: flex; flex-direction: row; justify-content: flex-start; align-items: center;">
                      云台摄像机
                      <cloud-file-icon style="margin-left: auto;" />
                    </div>
                  </div>
                </dv-border-box-12>
              </div>
            </div>

          </div>
        </div>
      </dv-border-box-10>
    </transition>
  </div>
</template>

<script>
import $ from "jquery";
import LeftTop from "@/components/LeftTop.vue";
import CameraIcon from "@/components/CameraIcon.vue";
import LightIcon from "@/components/LightIcon.vue";
import BrushIcon from "@/components/BrushIcon.vue";
import LoopIcon from "@/components/LoopIcon.vue";
import SplitScreenIcon from "@/components/SplitScreenIcon.vue";
import CloudFileIcon from "@/components/CloudFileIcon.vue";
import { color } from "echarts";
function formatter(number) {
  const numbers = number.toString().split("").reverse();
  const segs = [];

  while (numbers.length) segs.push(numbers.splice(0, 3).join(""));

  return segs.join(",").split("").reverse().join("");
}
export default {
  name: "Index",
  data() {
    return {
      activeName: "first",
      activeName2: "first",
    };
  },
  mounted() {
    // 百度地图API功能
    var map = new BMap.Map("map");
    var point = new BMap.Point(116.404, 39.915);
    map.centerAndZoom(point, 15);
    map.enableScrollWheelZoom(true);
    // 设置地图类型为混合地图
    map.setMapType(BMAP_HYBRID_MAP);
  },
  methods: {
    setBarData() {
      $(document).ready(() => {
        var chartDom = this.$refs.firstMain;
        var myChart = this.$echarts.init(chartDom);
        var option = {
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'cross',
              crossStyle: {
                color: '#999'
              }
            }
          },
          toolbox: {
            feature: {
              dataView: { show: false, readOnly: false },
              magicType: { show: true, type: ['line', 'bar'] },
              restore: { show: false },
              saveAsImage: { show: false }
            }
          },
          legend: {
            data: ['Evaporation', 'Precipitation', 'Temperature'],
            textStyle: {
              color: '#ffffff',
            }
          },
          xAxis: [
            {
              type: 'category',
              data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
              axisPointer: {
                type: 'shadow'
              },
              show: false
            }
          ],
          yAxis: [
            {
              type: 'value',
              name: 'Precipitation',
              nameTextStyle: {
                color: '#ffffff',
              },
              min: 0,
              max: 250,
              interval: 50,
              axisLabel: {
                formatter: '{value} ml',
                color: '#ffffff',
                fontSize: 10
              }
            },
            {
              type: 'value',
              name: 'Temperature',
              nameTextStyle: {
                color: '#ffffff'
              },
              min: 0,
              max: 25,
              interval: 5,
              axisLabel: {
                formatter: '{value} °C',
                color: '#ffffff',
                fontSize: 10
              }
            }
          ],
          series: [
            {
              name: 'Evaporation',
              type: 'bar',
              tooltip: {
                valueFormatter: function (value) {
                  return value + ' ml';
                }
              },
              data: [
                2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3
              ]
            },
            {
              name: 'Precipitation',
              type: 'bar',
              tooltip: {
                valueFormatter: function (value) {
                  return value + ' ml';
                }
              },
              data: [
                2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3
              ]
            },
            {
              name: 'Temperature',
              type: 'line',
              yAxisIndex: 1,
              tooltip: {
                valueFormatter: function (value) {
                  return value + ' °C';
                }
              },
              data: [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
            }
          ]
        };

        option && myChart.setOption(option);
      });
    },
    setBarData2() {
      $(document).ready(() => {
        var chartDom = this.$refs.thirdMain;
        var myChart = this.$echarts.init(chartDom);
        var option = {
          grid: {
            top: "10%",
            left: "22%",
            right: "14%",
            bottom: "10%"
            // containLabel: true
          },
          // 不显示x轴的相关信息
          xAxis: {
            show: false
          },
          yAxis: [
            {
              type: "category",
              inverse: true,
              data: ["电池电压(V)", "盐度(%)", "溶解氧(mg/L)", "浊度(NTU)", "pH", "水温(°C)"],
              // 不显示y轴的线
              axisLine: {
                show: false
              },
              // 不显示刻度
              axisTick: {
                show: false
              },
              // 把刻度标签里面的文字颜色设置为白色
              axisLabel: {
                color: "#fff",

              }
            },
            {
              data: [25.90, 34.16, 0.00, 2.05, 8.37, 15],
              inverse: true,
              // 不显示y轴的线
              axisLine: {
                show: false
              },
              // 不显示刻度
              axisTick: {
                show: false
              },
              // 把刻度标签里面的文字颜色设置为白色
              axisLabel: {
                color: function (value, index) {
                  // params 传进来的是柱子对象
                  // dataIndex 是当前柱子的索引号
                  let myColor = ['#fbaf16', '#73b73e', '#ff0000', '#73b73e', '#73b73e', '#ffffff'];
                  return myColor[index];
                },
              }
            }
          ],
          series: [
            {
              name: "条",
              type: "bar",
              data: [25.90, 34.16, 0.00, 2.05, 8.37, 15],
              yAxisIndex: 0,
              // 修改第一组柱子的圆角
              itemStyle: {
                barBorderRadius: 20,
                // 此时的color 可以修改柱子的颜色
                color: '#00A86B'
              },
              // 柱子之间的距离
              barCategoryGap: 50,
              //柱子的宽度
              barWidth: 10,
              // 显示柱子内的文字
              label: {
                show: false,
                position: "inside",
                // {c} 会自动的解析为 数据  data里面的数据
                formatter: "{c}%"
              }
            },
            {
              name: "框",
              type: "bar",
              barCategoryGap: 50,
              barWidth: 15,
              yAxisIndex: 1,
              data: [37, 37, 37, 37, 37, 37],
              itemStyle: {
                color: "none", // 不要条的颜色
                borderColor: "#00c1de",
                borderWidth: 3,
                barBorderRadius: 15
              }
            }
          ]
        };

        option && myChart.setOption(option);
      });
    },
    handleClick(tab, event) {
      // console.log(tab, event);
    },
    handleClick2(tab, event) {
      // console.log(tab, event);
    },
  },
  async created() {
    $(document).ready(async () => {
      this.setBarData()
      this.setBarData2()
    })
  },
  components: {
    LeftTop,
    CameraIcon,
    LightIcon,
    BrushIcon,
    LoopIcon,
    SplitScreenIcon,
    CloudFileIcon
  },
};
</script>

<style lang="less" scoped>
#sixthMain {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.rounded-box {
  background-color: rgb(7, 76, 140);
  /* 天蓝色背景 */
  border-radius: 10px;
  /* 圆角 */
  color: white;
  /* 白色文字 */
  font-size: 15px;
  /* 字体大小 */
  font-weight: bold;
  /* 字体加粗 */
  padding: 20px;
  /* 内边距 */
  width: calc(63.33% - 5px);
  /* 设置盒子的宽度，使得每行可以放置三个盒子 */
  margin-bottom: 8px;
  /* 添加底部边距，使得两行之间有空间 */
  height: 35px;
  margin-left: 12%;
  margin-top: 8px;
}

::v-deep .el-tabs__item.is-active {
  color: #4b83f2; //当前标签页颜色
}

::v-deep .el-tabs__item {
  color: #bfc0c2; //标签页默认颜色
  font-weight: bold;
  font-size: 15px;
}

::v-deep .el-tabs__item:hover {
  color: #bfc0c2; //鼠标悬停标签页变化的颜色
}

.loading {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.cent-1-content {
  padding: 20px;
  display: flex;
}

.right-content {
  margin-left: 30px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.right-content div {
  display: flex;
  font-size: 15px;
  align-items: center;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

// .cents {
//   display: flex;
//   flex-direction: column;
// }

.above {
  display: flex;
}

.aboveOne {
  display: flex;
  flex-direction: column;
}

.aboveTwo {
  display: flex;
  flex-direction: column;
}

// .cent {
//   width: 850px;
//   height: 300px;
// }

.cent-1 {
  margin: 10px;
  color: aliceblue;
  width: 500px;
  height: 220px;
  /* background-color: rgb(26, 26, 133); */
}

.left {
  display: flex;
  flex-direction: column;
}

.cent {
  display: flex;
  flex-direction: column;
}

.right {
  display: flex;
  flex-direction: column;
}

.left-1 {
  margin: 5px;
  color: aliceblue;
  width: 550px;
  display: flex;
  flex-direction: column;
}

.left-2 {
  margin: 5px;
  color: aliceblue;
  width: 530px;
  display: flex;
  flex-direction: column;
}

.col-1 {
  margin-right: 30px;
  color: aliceblue;
  width: 430px;
  display: flex;
  flex-direction: column;
}

.col-2 {
  margin-left: 30px;
  margin-right: 55px;
  color: aliceblue;
  width: 300px;
  display: flex;
  flex-direction: column;
}

.col-3 {
  margin-left: 55px;
  color: aliceblue;
  width: 540px;
  display: flex;
  flex-direction: column;
}

.naca {
  // padding: 35px 15px 0 15px;
  box-sizing: border-box;
  width: 100%;
  // height: 40rem;
  display: flex;
  flex-direction: column;
}

.naca .index-header {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.naca .index-header div {
  display: flex;
  justify-content: center;
  align-items: center;
}

.naca .index-content {
  display: flex;
  justify-content: center;
  align-items: center;
}

.bg {
  width: 100%;
  height: 45rem;
  background-color: black;
  position: relative;
}

.title {
  color: #3f96a5;
  font-size: 18px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-weight: bold;
}

.content {
  display: flex;
  align-items: center;
}

.content-word {
  width: 140px;
  height: 130px;
  background: #11193e;
  border-radius: 40px;
  border: 1px solid #3d3d3d;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.content-word-item {
  margin-left: 19px;
  margin-bottom: 10px;

  img {
    width: 20px;
    height: 20px;
  }
}

.content-word-item-title {
  font-size: 18px;
}

.content-word-item-content {
  margin-top: 5px;

  display: flex;
  align-items: center;
}

.row_list {
  list-style: none;
}

.cases_list::-webkit-scrollbar {
  display: none;
}

.cases_list li {
  display: grid;
  -ms-grid-columns: 30px 110px 60px 60px 60px 50px 100px;
  grid-template-columns: 30px 110px 60px 60px 60px 50px 100px;
  cursor: pointer;
  margin-left: 23px;
  text-align: center;
  line-height: 30px;
  color: rgb(238, 236, 236);
}

.list_time {
  height: 30px;
  overflow: auto;
}

.list_time::-webkit-scrollbar {
  display: none;
}
</style>