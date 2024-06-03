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
                水下系统
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
              <div class="left-1" style="">
                <dv-border-box-11 style="height: 200px; width: 490px; color: white;">
                  <div style="padding: 5px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                    <div class="title" style="margin-top: 5px; ; color: white; text-align: center;"> <!-- 文本框标题居中 -->
                      鱼群数量
                    </div>
                    <dv-decoration-7 style="width:400px;height: 60px; margin: 8px 0; font-size: 24px;">总数：{{ today }}</dv-decoration-7> <!-- 增大字体 -->
                    <div style="display: flex; justify-content: center;"> <!-- 第二、三个文本框并列排布 -->
                      <dv-decoration-7 style="width: 200px; height: 50px; margin-right: 10px; font-size: 18px;">今日新增：{{ todayAdded }}</dv-decoration-7> <!-- 增大字体 -->
                      <dv-decoration-7 style="width: 200px; height: 50px; font-size: 18px;">今日死亡：{{ todayDead }}</dv-decoration-7> <!-- 增大字体 -->
                    </div>
                  </div>
                </dv-border-box-11>

                <dv-border-box-12 style="height: 200px; width: 490px; color: white;">
                  <div class="title" style="margin-top: 5px;">
                    海洋牧场环境感知得分
                  </div>
                  <div style="width: 100%; height: 5%; color: white; text-align: right; color: white;">
                    <div style="opacity: 0.4;">舒适: 维持良好状态</div>
                    <div style="opacity: 0.4;">正常: 可能出现轻微变化或趋势</div>
                    <div style="opacity: 0.4;">隐患: 环境存在明显变化或问题</div>
                    <div style="opacity: 0.4;">危险: 出现严重问题或危机</div>
                  </div>
                  <div
                    ref="environment_count1"
                    style="width: 100%; height: 100%; color: white;"
                  ></div>
                </dv-border-box-12>

               <div>


  <dv-border-box-12 style="height: 300px; width: 490px;">
    <div class="title" style="margin-top: 5px">鱼群个体数量历史曲线</div>
    <!-- <div ref="timeZhou" style="width: 100%; height: 300px"></div> -->
    <div
      ref="history"
      style="width: 100%; height: 300px"
    />
  </dv-border-box-12>

</div>


              </div>
            </div>

            <div class="cent">
       
<dv-border-box-12 style="height: 330px; width: 540px; display: flex; flex-direction: column; align-items: center;">
  <div style="margin-top: 20px; display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <div class="title" style="margin-top: 5px; text-align: center;color: white;">数据统计</div>
    <div style="text-align: center; display: flex; justify-content: space-between; align-items: center; width: 100%;">
      <div style="display: flex; flex-direction: column; align-items: center; margin-bottom: 20px;">
        <dv-decoration-7 style="width: 150px; height: 30px;color: white;">鱼种:{{ fishType }}</dv-decoration-7>
        <dv-decoration-7 style="width: 150px; height: 30px;color: white;">鱼苗:{{ fry }}尾</dv-decoration-7>
        <dv-decoration-7 style="width: 150px; height: 30px;color: white;">生长:{{ growth }}尾</dv-decoration-7>
      </div>
      <dv-decoration-9 style="width: 200px; height: 200px; color: #fff; font-weight: bold; font-size: 20px;">已保障养殖鱼尾数：<br>{{ statistic }}</dv-decoration-9>
      <div style="display: flex; flex-direction: column; align-items: center; margin-bottom: 20px;">
        <dv-decoration-7 style="width: 150px; height: 30px;color: white;">镜头：{{ camera }}</dv-decoration-7>
        <dv-decoration-7 style="width: 150px; height: 30px;color: white;">云台：{{ platform }}</dv-decoration-7>
        <dv-decoration-7 style="width: 150px; height: 30px;color: white;">声纳：{{ sonar }}</dv-decoration-7>
      </div>
    </div>
  </div>
</dv-border-box-12>



              <dv-border-box-12 style="height: 220px; width: 540px">
                <div class="title" style="margin-top: 5px">鱼群属性分布曲线</div>
			  </dv-border-box-12> 
             

			 </div>



            <div class="right">
              <div class="col-2" style="">

<dv-border-box-11>
  <div style="padding: 15px">
    <div class="title" style="margin-top: 5px; color: white;"> <!-- 白色字体 -->
      硬件信息
    </div>
    <div id="secondMain" style="width: 100%; height: auto; display: flex; justify-content: space-between;"> <!-- Added justify-content: space-between -->
      <div style="width: 48%; display: flex; flex-direction: column;"> <!-- Adjusted width and added flex-direction -->
        <dv-decoration-11 style="height:60px; color: white;">网箱信息</dv-decoration-11> <!-- Removed width -->
        <div>
          <dv-decoration-7 style="height:30px; color: white;">长度：{{ cageLength }}</dv-decoration-7> <!-- Removed width -->
          <dv-decoration-7 style="height:30px; color: white;">宽度：{{ cageWidth }}</dv-decoration-7> <!-- Removed width -->
          <dv-decoration-7 style="height:30px; color: white;">深度：{{ cageDepth }}</dv-decoration-7> <!-- Removed width -->
          <dv-decoration-7 style="height:30px; color: white;">经度：{{ longitude }}</dv-decoration-7> <!-- Removed width -->
          <dv-decoration-7 style="height:30px; color: white;">纬度：{{ latitude }}</dv-decoration-7> <!-- Removed width -->
        </div>
      </div>
      <div style="width: 48%; display: flex; flex-direction: column;"> <!-- Adjusted width and added flex-direction -->
        <dv-decoration-11 style="height:60px; color: white;">水底传感器</dv-decoration-11> <!-- Removed width -->
        <div>
          <dv-decoration-7 style="height:30px; color: white;">运行时间：{{ runtime }}</dv-decoration-7> <!-- Removed width -->
          <dv-decoration-7 style="height:30px; color: white;">下次检修：{{ nextMaintenance }}</dv-decoration-7> <!-- Removed width -->
          <dv-decoration-7 style="height:30px; color: white;">保修过期：{{ warrantyExpired }}</dv-decoration-7> <!-- Removed width -->
          <dv-decoration-7 style="height:30px; color: white;">保修过期：{{ warrantyExpired }}</dv-decoration-7> <!-- Removed width -->
		</div>
      </div>
    </div>
  </div>
</dv-border-box-11>

                
                      <dv-border-box-12>
                              <div style="padding: 5px">
                              <div class="title" style="margin-top: 5px">
                                  鱼群种类占比
                                </div>
                            <div ref="thirdMain" style="width: 100%; height: 150px"></div>
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
	  today: 1038, // 今日数量
      todayAdded: 20, // 今日新增
      todayDead: 5, // 今日死亡

      statistic: 159485,
	  fishType: 50,
	  fry: 500,
	  growth: 600,
	  camera: 5,
	  platform: 2,
	  sonar: 1,

      cageLength: '100m', // 网箱长度
      cageWidth: '50m', // 网箱宽度
      cageDepth: '20m', // 网箱深度
      longitude: '128.034', // 经度
      latitude: '56.123', // 纬度
      runtime: '24天13小时56分钟', // 运行时间
      nextMaintenance: '35天后', // 下次检修时间
      warrantyExpired: '2035年10月9日', // 保修过期时间
      

    }
  },


  methods: {

    environment_point() {
      $(document).ready(() => {
		var chartDom = this.$refs.environment_count1;
        chartDom.style.width = '490px'; // 设置宽度
        chartDom.style.height = '200px'; // 设置高度
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
                    return "舒适";
                  } else if (value === 0.625) {
                    return "正常";
                  } else if (value === 0.375) {
                    return "隐患";
                  } else if (value === 0.125) {
                    return "危险";
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
                  name: "环境评估",
                },
              ],
            },
          ],
        };

        option && myChart.setOption(option);
      });
    },

history() {
   var chartDom = this.$refs.history;
   chartDom.style.width = '490px'; // 设置宽度
   chartDom.style.height = '270px'; // 设置高度
   var myChart = this.$echarts.init(chartDom);
   var option;

   let base = +new Date(2017, 9, 3);
   let oneDay = 24 * 3600 * 1000;
   let data = [[base, Math.random() * 300]];
   let currentDate = new Date(); // 获取当前时间
   for (let i = 1; i < 20000; i++) {
      let now = new Date((base += oneDay));
      if (now > currentDate) { // 如果超过当前时间则停止添加数据
         break;
      }
      data.push([+now, Math.round((Math.random() - 0.5) * 20 + data[i - 1][1])]);
   }
   option = {
      tooltip: {
         trigger: 'axis',
         position: function (pt) {
            return [pt[0], '10%'];
         }
      },
      toolbox: {
         feature: {
            dataZoom: {
               yAxisIndex: 'none'
            },
            restore: {},
            saveAsImage: {}
         }
      },
      xAxis: {
         type: 'time',
         boundaryGap: false
      },
      yAxis: {
         type: 'value',
         boundaryGap: [0, '100%'],
         min: 0  // 设置最小值为 0
      },
      dataZoom: [
         {
            type: 'inside',
            start: 0,
            end: 20
         },
         {
            start: 0,
            end: 20
         }
      ],
      series: [
         {
            name: '鱼尾数',
            type: 'line',
            smooth: true,
            symbol: 'none',
            areaStyle: {},
            data: data
         }
      ]
   };
   option && myChart.setOption(option);
},

    setpieData() {
      $(document).ready(() => {
        var chartDom = this.$refs.thirdMain;
        var myChart = this.$echarts.init(chartDom);
        var option;
        var option = {
          tooltip: {
            trigger: 'item',
            formatter: "{a}<br/>{b}: {c}({d}%)"
          },
          toolbox: {
            show: true
          },
          calulable: true,

          legend: {
            orient: 'vertical',
            left: 'left',
            top: 'center',
            data: ['大黄鱼', '鲈鱼', '石斑鱼', '鲷鱼', '军曹鱼']
          },
          series: [
            {
              name: '数量',
              type: 'pie',
              radius: ['40%', '70%'],
              avoidLabelOverlap: false,
              label: {
                show: false,
                position: 'center'
              },
              emphasis: {
                label: {
                  show: true,
                  fontSize: 15,
                  fontWeight: 'bold'
                }
              },
              labelLine: {
                show: false
              },
              data: [
                { value: 19798, name: '大黄鱼' },
                { value: 16658, name: '鲈鱼' },
                { value: 15957, name: '石斑鱼' },
                { value: 8837, name: '鲷鱼' },
                { value: 38831, name: '军曹鱼' }
              ]
            }
          ]
        };

        option && myChart.setOption(option);
      });
    },
  },
  async created() {
    $(document).ready(async () => {
      this.environment_point();
	  this.history();
	  this.setpieData();
    })
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
  width: 600px;
  display: flex;
  flex-direction: column;
}

.left-2 {
  margin: 5px;
  color: aliceblue;
  width: 600px;
  display: flex;
  flex-direction: column;
}

.col-1 {
  margin-right: 30px;
  color: aliceblue;
  width: 440px;
  display: flex;
  flex-direction: column;
}

.col-2 {
  margin-left: 30px;
  margin-right: 55px;
  color: aliceblue;
  width: 330px;
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