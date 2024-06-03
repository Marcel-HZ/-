<template>
  <div class="home">
    <transition name="fade" mode="out-in">
      <dv-border-box-10>
        <div class="naca">
          <div class="index-header" style="margin-top: 5px">
            <div>
              <dv-decoration-10
                style="width: 450px; height: 1px; margin-bottom: 45px"
              />
              <dv-decoration-8
                style="width: 180px; height: 50px"
                :color="['#568aea', '#000000']"
              />
              <div
                style="
                  width: 150px;
                  color: #eeecec;
                  font-size: 18px;
                  padding: 0 15px;
                  font-weight: bold;
                "
              >
                可视化化平台
              </div>
              <dv-decoration-8
                :reverse="true"
                style="width: 180px; height: 50px"
                :color="['#568aea', '#000000']"
              />
              <dv-decoration-10
                style="
                  width: 450px;
                  height: 1px;
                  transform: rotateY(180deg);
                  margin-bottom: 45px;
                "
              />
            </div>
            <dv-decoration-5
              style="width: 10%; height: 20px"
              :color="['#568aea', '#000000']"
            />
          </div>

          <div class="index-content">
            <div class="left">
              <div class="col-1" style="">
                <dv-border-box-12
                  style="height: 300px; width: 490px ;color=white"
                >
                  <div class="title" style="margin-top: 5px">
                    海洋牧场环境感知得分
                  </div>
                  <div
                    style="
                      width: 100%;
                      height: 5%;
                      color: white;
                      text-align: center;
                    "
                  >
                    <div>A: 环境优良，维持良好状态</div>
                    <div>B 环境一般，可能出现轻微变化或趋势</div>
                    <div>C: 环境较差，存在明显变化或问题</div>
                    <div>D: 环境恶化，出现严重问题或危机</div>
                  </div>
                  <div
                    ref="environment_count1"
                    style="width: 100%; height: 105%;color=white"
                  ></div>
                </dv-border-box-12>

                <dv-border-box-12 style="height: 250px; width: 490px">
                  <div class="title" style="margin-top: 5px">网衣/鱼群检测</div>
                  <div ref="secondMain" style="width: 70%; height: 100%">
                    <div
                      ref="fishChart"
                      style="width: 150%; height: 105%;color=white"
                    ></div>
                  </div>
                </dv-border-box-12>
              </div>
            </div>

            <div class="cent">
              <div class="col-3" style="">
                <dv-border-box-12 style="height: 330px; width: 540px">
                  <div class="title" style="margin-top: 5px">图像识别</div>
                  <div
                    style="
                      display: flex;
                      justify-content: space-between;
                      width: 100%;
                    "
                  >
                    <div
                      id="fifthMain"
                      style="
                        width: 170%;
                        height: 270px;
                        margin-top: 10px;
                        background: black;
                      "
                    >
                      <div class="title" style="margin-top: 5px">识别效果</div>
                    </div>
                    <div
                      style="
                        display: flex;
                        flex-direction: column;
                        justify-content: space-between;
                        width: 100%;
                      "
                    >
                      <div style="width: 90%; height: 150px; background: black">
                        <div class="title" style="margin-top: 5px">
                          左目镜头
                        </div>
                      </div>
                      <div style="width: 90%; height: 150px; background: black">
                        <div class="title" style="margin-top: 5px">
                          右目镜头
                        </div>
                      </div>
                    </div>
                  </div>
                </dv-border-box-12>

                <dv-border-box-12 style="height: 220px; width: 540px">
                  <div class="title" style="margin-top: 5px">实时数据</div>
                  <div
                    id="sixthMain"
                    style="
                      display: grid;
                      grid-template-columns: repeat(3, 1fr);
                      width: 98%;
                      height: 90%;
                    "
                  >
                    <div
                      class="rounded-box"
                      style="
                        display: flex;
                        flex-direction: row;
                        justify-content: flex-start;
                        align-items: center;
                      "
                    >
                      编号
                      <camera-icon style="margin-left: auto" />
                      <span id="fishId">Fish 001</span>
                    </div>
                    <div
                      class="rounded-box"
                      style="
                        display: flex;
                        flex-direction: row;
                        justify-content: flex-start;
                        align-items: center;
                      "
                    >
                      鱼种
                      <light-icon style="margin-left: auto" />
                      <span id="fishSpecies">Goldfish</span>
                    </div>
                    <div
                      class="rounded-box"
                      style="
                        display: flex;
                        flex-direction: row;
                        justify-content: flex-start;
                        align-items: center;
                      "
                    >
                      体长
                      <brush-icon style="margin-left: auto" />
                      <span id="fishLength">10 cm</span>
                    </div>
                    <div
                      class="rounded-box"
                      style="
                        display: flex;
                        flex-direction: row;
                        justify-content: flex-start;
                        align-items: center;
                      "
                    >
                      疑似病患
                      <loop-icon style="margin-left: auto" />
                      <span id="suspiciousCases">2</span>
                    </div>
                    <div
                      class="rounded-box"
                      style="
                        display: flex;
                        flex-direction: row;
                        justify-content: flex-start;
                        align-items: center;
                      "
                    >
                      鱼群异常
                      <split-screen-icon style="margin-left: auto" />
                      <span id="abnormalSchools">1</span>
                    </div>
                    <div
                      class="rounded-box"
                      style="
                        display: flex;
                        flex-direction: row;
                        justify-content: flex-start;
                        align-items: center;
                      "
                    >
                      轨迹分析
                      <cloud-file-icon style="margin-left: auto" />
                      <span id="trajectoryAnalysis">Available</span>
                    </div>
                  </div>
                </dv-border-box-12>
              </div>
            </div>

            <div class="right">
              <div class="col-2" style="">
                <dv-border-box-12 style="height: 300px; width: 410px">
                  <div
                    style="
                      display: flex;
                      flex-direction: column;
                      justify-content: space-between;
                      width: 100%;
                    "
                  >
                    <div
                      style="
                        width: 90%;
                        height: 190px;
                        border-radius: 10px;
                        margin: 0 auto;
                      "
                    >
                      <div class="title" style="margin-top: 5px">AI决策</div>
                      <div
                        style="
                          display: flex;
                          flex-wrap: wrap;
                          justify-content: space-around;
                        "
                      >
                        <div
                          style="
                            width: 100%;
                            height: 5%;
                            color: white;
                            text-align: center;
                            font-size: 16px;
                          "
                        >
                          <div>
                            温度：
                            <span id="temperatureValue">20°C - 30°C</span>
                          </div>
                          <div>
                            光照：
                            <span id="lightValue">500 lux - 1000 lux</span>
                          </div>
                          <div>
                            溶解氧：
                            <span id="oxygenValue">6 mg/L - 8 mg/L</span>
                          </div>
                          <div>
                            盐度：
                            <span id="salinityValue">25 ppt - 35 ppt</span>
                          </div>
                          <div>pH： <span id="phValue">pH 7 - pH 8</span></div>
                        </div>
                      </div>
                    </div>
                    <div style="width: 90%; height: 50px">
                      <div class="title" style="margin-top: 5px">提示</div>
                      <div
                        style="
                          width: 100%;
                          height: 5%;
                          color: white;
                          text-align: center;
                          font-size: 16px;
                        "
                      >
                        未来几天可能降雨，请保持温度风度正常
                      </div>
                      <div></div>
                    </div>
                  </div>
                </dv-border-box-12>

                <dv-border-box-12 style="height: 250px; width: 410px">
                  <div
                    ref="fourthMain"
                    style="width: 93%; height: 83%; margin-left: 15px"
                  >
                    <div
                      style="
                        display: flex;
                        justify-content: space-between;
                        width: 100%;
                      "
                    >
                      <div style="width: calc(50% - 10px); border-radius: 10px">
                        <div class="title" style="margin-top: 5px">
                          气象数据
                        </div>
                        <div
                          id="sixthMain"
                          style="
                            display: grid;
                            grid-template-columns: repeat(2, 1fr);
                            grid-template-rows: repeat(2, auto);
                            gap: 20px;
                          "
                        >
                          <div
                            class="rounded-box"
                            style="display: flex; align-items: center"
                          >
                            温度
                            <temperature-icon
                              style="margin-left: auto"
                            ></temperature-icon>
                            <span id="temperatureValue">20°C - 30°C</span>
                          </div>
                          <div
                            class="rounded-box"
                            style="display: flex; align-items: center"
                          >
                            风向
                            <wind-icon style="margin-left: auto"></wind-icon>
                            <span id="windDirection">北风</span>
                          </div>
                          <div
                            class="rounded-box"
                            style="display: flex; align-items: center"
                          >
                            湿度
                            <humidity-icon
                              style="margin-left: auto"
                            ></humidity-icon>
                            <span id="humidityValue">60%</span>
                          </div>
                          <div
                            class="rounded-box"
                            style="display: flex; align-items: center"
                          >
                            空气污染
                            <pollution-icon
                              style="margin-left: auto"
                            ></pollution-icon>
                            <span id="pollutionLevel">中度污染</span>
                          </div>
                        </div>
                      </div>
                      <div
                        style="
                          width: 40%;
                          height: 5%;
                          color: white;
                          text-align: center;
                          font-size: 16px;
                        "
                      >
                        <div class="title" style="margin-top: 5px; color: red">
                          警报
                        </div>
                        <div>
                          海啸警报
                          <span id="tsunami_alert"
                            >紧急行动通知！预计于05月12日上午10:30在沿海地区发生6级海啸。立即疏散至高处，确保安全。</span
                          >
                        </div>
                      </div>
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
    return {};
  },
  methods: {
    environment_point() {
      $(document).ready(() => {
        var chartDom = this.$refs.environment_count1;
        var myChart = this.$echarts.init(chartDom);
        var option;

        option = {
          series: [
            {
              type: "gauge",
              startAngle: 180,
              endAngle: 0,
              center: ["50%", "75%"],
              radius: "90%",
              min: 0,
              max: 1,
              splitNumber: 8,
              axisLine: {
                lineStyle: {
                  width: 6,
                  color: [
                    [0.25, "#FF6E76"],
                    [0.5, "#FDDD60"],
                    [0.75, "#58D9F9"],
                    [1, "#7CFFB2"],
                  ],
                },
              },
              pointer: {
                icon: "path://M12.8,0.7l12,40.1H0.7L12.8,0.7z",
                length: "12%",
                width: 20,
                offsetCenter: [0, "-60%"],
                itemStyle: {
                  color: "auto",
                },
              },
              axisTick: {
                length: 12,
                lineStyle: {
                  color: "auto",
                  width: 2,
                },
              },
              splitLine: {
                length: 20,
                lineStyle: {
                  color: "auto",
                  width: 5,
                },
              },
              axisLabel: {
                color: "#464646",
                fontSize: 20,
                distance: -60,
                rotate: "tangential",
                formatter: function (value) {
                  if (value === 0.875) {
                    return "Grade A";
                  } else if (value === 0.625) {
                    return "Grade B";
                  } else if (value === 0.375) {
                    return "Grade C";
                  } else if (value === 0.125) {
                    return "Grade D";
                  }
                  return "";
                },
              },
              title: {
                offsetCenter: [0, "-10%"],
                fontSize: 20,
              },
              detail: {
                fontSize: 30,
                offsetCenter: [0, "-35%"],
                valueAnimation: true,
                formatter: function (value) {
                  return Math.round(value * 100) + "";
                },
                color: "inherit",
              },
              data: [
                {
                  value: 0.7,
                  name: "Grade Rating",
                },
              ],
            },
          ],
        };

        option && myChart.setOption(option);
      });
    },
    setLineData() {
      $(document).ready(() => {
        var chartDom = this.$refs.AIcontest;
        var myChart = this.$echarts.init(chartDom);
        var option;
        option = {
          title: {
            text: "",
            textStyle: {
              color: "#fff", // 设置标题字体颜色为白色
            },
          },
          tooltip: {
            trigger: "axis",
            textStyle: {},
          },
          legend: {
            data: ["水温", "PH值", "溶解氧", "营养盐", "浊度"],
            textStyle: {
              color: "#fff", // 设置图例字体颜色为白色
            },
          },
          grid: {
            left: "3%",
            right: "4%",
            bottom: "3%",
            containLabel: true,
          },
          toolbox: {
            feature: {
              saveAsImage: {},
            },
          },
          xAxis: {
            type: "category",
            boundaryGap: false,
            data: ["周一", "周二", "周三", "周四", "周五", "周六", "周日"],
            axisLabel: {
              color: "#fff", // 设置x轴标签字体颜色为白色
            },
          },
          yAxis: {
            type: "value",
            axisLabel: {
              color: "#fff", // 设置y轴标签字体颜色为白色
            },
          },
          series: [
            {
              name: "水温",
              type: "line",
              data: [25, 26, 27, 25, 26, 25, 24],
            },
            {
              name: "PH值",
              type: "line",
              data: [7.2, 7.4, 7.3, 7.1, 7.5, 7.2, 7.0],
            },
            {
              name: "溶解氧",
              type: "line",
              data: [8.5, 8.2, 8.7, 8.3, 8.1, 8.6, 8.4],
            },
            {
              name: "营养盐",
              type: "line",
              data: [0.5, 0.6, 0.4, 0.7, 0.3, 0.5, 0.6],
            },
            {
              name: "浊度",
              type: "line",
              data: [10, 12, 8, 14, 9, 11, 13],
            },
          ],
        };

        option && myChart.setOption(option);
      });
    },
    setFishdata() {
      $(document).ready(() => {
        var chartDom = this.$refs.fishChart;
        var myChart = this.$echarts.init(chartDom);
        var option;

        // prettier-ignore
        const data = [["2000-06-05", 116], ["2000-06-06", 129], ["2000-06-07", 135], ["2000-06-08", 86], ["2000-06-09", 73], ["2000-06-10", 85], ["2000-06-11", 73], ["2000-06-12", 68], ["2000-06-13", 92], ["2000-06-14", 130], ["2000-06-15", 245], ["2000-06-16", 139], ["2000-06-17", 115], ["2000-06-18", 111], ["2000-06-19", 309], ["2000-06-20", 206], ["2000-06-21", 137], ["2000-06-22", 128], ["2000-06-23", 85], ["2000-06-24", 94], ["2000-06-25", 71], ["2000-06-26", 106], ["2000-06-27", 84], ["2000-06-28", 93], ["2000-06-29", 85], ["2000-06-30", 73], ["2000-07-01", 83], ["2000-07-02", 125], ["2000-07-03", 107], ["2000-07-04", 82], ["2000-07-05", 44], ["2000-07-06", 72], ["2000-07-07", 106], ["2000-07-08", 107], ["2000-07-09", 66], ["2000-07-10", 91], ["2000-07-11", 92], ["2000-07-12", 113], ["2000-07-13", 107], ["2000-07-14", 131], ["2000-07-15", 111], ["2000-07-16", 64], ["2000-07-17", 69], ["2000-07-18", 88], ["2000-07-19", 77], ["2000-07-20", 83], ["2000-07-21", 111], ["2000-07-22", 57], ["2000-07-23", 55], ["2000-07-24", 60]];
        const dateList = data.map(function (item) {
          return item[0];
        });
        const valueList = data.map(function (item) {
          return item[1];
        });
        option = {
          visualMap: [
            {
              show: false,
              type: "continuous",
              seriesIndex: 0,
              min: 0,
              max: 400,
            },
            {
              show: false,
              type: "continuous",
              seriesIndex: 1,
              dimension: 0,
              min: 0,
              max: dateList.length - 1,
            },
          ],
          title: [
            {
              left: "center",
              text: "鱼群数量",
              textStyle: {
                color: "#ffffff",
              },
            },
            {
              top: "55%",
              left: "center",
              text: "鱼群活跃度",
              textStyle: {
                color: "#ffffff",
              },
            },
          ],
          tooltip: {
            trigger: "axis",
          },
          xAxis: [
            {
              data: dateList,
            },
            {
              data: dateList,
              gridIndex: 1,
            },
          ],
          yAxis: [
            {},
            {
              gridIndex: 1,
            },
          ],
          grid: [
            {
              bottom: "60%",
            },
            {
              top: "60%",
            },
          ],
          series: [
            {
              type: "line",
              showSymbol: false,
              data: valueList,
            },
            {
              type: "line",
              showSymbol: false,
              data: valueList,
              xAxisIndex: 1,
              yAxisIndex: 1,
            },
          ],
        };

        option && myChart.setOption(option);
      });
    },
  },
  async created() {
    $(document).ready(async () => {
      this.setLineData();
      this.setFishdata();
      this.environment_point();
    });
  },
  components: {
    LeftTop,
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
