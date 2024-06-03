<template>
  <div class="home">
    <transition name="fade" mode="out-in">
     
      <dv-border-box-10
        ><div class="naca">
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
                数据中心
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
               
                <dv-border-box-12><div style="padding: 5px">
                  <div class="title" style="margin-top: 5px">
                    各种鱼群的数量
                  </div>

                  <div ref="firstMain" style="width: 100%; height: 120px"></div>
                </div></dv-border-box-12>
                <dv-border-box-12><div style="padding: 5px;padding-bottom:30px">
                  <div class="title" style="margin-top: 1px">水质数据</div>
                  <dv-scroll-board
                    :config="config1"
                    style="width: 100%; height: 110px"
                  />
                </div></dv-border-box-12>
     
                
                <dv-border-box-8><div style="padding: 15px">
                  <div class="title" style="margin-top: 5px">传感器信息</div>
                  <!-- <div ref="timeZhou" style="width: 100%; height: 350px"></div> -->
                  <dv-scroll-board
                    :config="config2"
                    style="width: 100%; height: 110px"
                  />
                </div></dv-border-box-8>
               

                
               



              </div>
            </div>
            <div class="cents">
              <div class="above">
                <div class="aboveOne">
                  <div style="padding: 15px">
                    <div class="title">系统信息</div>
                    <div
                      style="
                        display: flex;
                        flex-direction: column;
                        width: 100%;
                        height: 120px;
                        color: #eeecec;
                      "
                    >
                       <div style="display: flex; flex: 1">
                        <dv-decoration-11 style="width：20px;height:60px;text-align:center;">cpu使用率</dv-decoration-11>
                       </div>
                      <div style="display: flex; flex: 1">
                      
                       <dv-decoration-9 style="width：150px;height:150px;">50%</dv-decoration-9>
                      </div>
                    </div>
                    
                  </div>
                  <div style="padding: 15px">
                    <div class="title" style="margin-top: -30px">
                     

                    </div>
                    <div class="content">
                      
                      <div style="width: 430px; height: 90px"></div>
                    </div>
                  </div>
                </div>
                <div class="aboveTwo">
              
                  <dv-border-box-12 > <div style="padding: 15px">
                  <div class="title" style="margin-top: 5px">
                   访问次数统计
                  </div>
               <dv-capsule-chart 
                    :config="config3" style="width:300px;height:40px" />

                  <div id="secondMian" style="width: 100%; height: 110px"></div>
                </div></dv-border-box-12>
                  <dv-border-box-12><div style="padding: 5px">
                    <div class="title" style="margin-top: 5px">
                      当日交互统计
                    </div>
                    <div
                      ref="thirdMain"
                      style="width: 400px; height: 80px"
                    ></div>
                  </div></dv-border-box-12>
                  
                </div>
              </div>
              <div class="below">
                
                  <dv-border-box-9 :color="['#568aea']">
                    <div style="padding: 7px">
                      <div class="title" style="margin-top: 5px">
                       数据中心分布 
                      </div>        
                      <dv-scroll-ranking-board :config="config4" style="width: 100%;height:140px;" />             
                      <div
                        ref="lastMain"
                        style="width: 100%; height: 60px; margin-top: 25px"
                      ></div>
                    </div>
                  </dv-border-box-9>
                
              </div>
            </div>
          </div></div
      ></dv-border-box-10>
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
  config1:{
     header: ['时间', 'PH', '溶解氧(mg/L)','温度(°C)','无机氮(mg/L)'],
      data: [
    ['2024-5-11', '7.80', '9.33','15','0.386'],
    ['2024-5-12', '9.83', '9.09','14','0.437'],
    ['2024-5-13', '7.91', '9.28','13','0.163'],
    ['2024-5-14', '8.03', '7.27','15','0.546'],
    ['2024-5-15', '8.13', '6.73','12','0.437'],
    ['2024-5-16', '7.98', '6.89','11','0.366'],
    ['2024-5-17', '8.03', '7.06','14','0.335'],
 ]
  },
config2:{
    header: ['设备', '编号', '类型','大小'],
  data: [
    ['水底摄像头', 'video-1', 'H.264','4Mb'],
    ['水底摄像头', 'video-2', '4CIF','128kb'],
    ['水面摄像头', 'video-3', 'H.264','100b'],
    ['云台', 'holder-1', 'H.264','1kb'],
    ['声纳', 'sonar-1', 'H.264','1kb'],
  ]
},
config3:{
   data: [
    {
      name: '星期一',
      value: 167
    },
    {
      name: '星期二',
      value: 67
    },
    {
      name: '星期三',
      value: 123
    },
    {
      name: '星期四',
      value: 55
    },
    {
      name: '星期五',
      value: 98
    },
    {
      name: '星期六',
      value: 167
    },
    {
      name: '星期日',
      value: 167
    }
  ],
   showValue: true
},
config4:{
    data: [
    {
      name: '北京',
      value: 55
    },
    {
      name: '上海',
      value: 120
    },
    {
      name: '海南',
      value: 78
    },
    {
      name: '厦门',
      value: 66
    },
    {
      name: '深圳',
      value: 80
    },
    {
      name: '贵阳',
      value: 45
    },
   
  ]
    }
    }
  },
methods:{
  
setWorData(){
  var chartDom=this.$refs.thirdMain
  var myChart=this.$echarts.init(chartDom)
  var option;

option = {
  xAxis: {
    type: 'category',
    data: ['查询次数','成功次数','失败次数','异常次数']
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      data: [567, 345,123,5],
      type: 'bar'
    }
  ]
};

option && myChart.setOption(option);
},

setpieData(){
$(document).ready(()=>{
    var chartDom = this.$refs.firstMain;
    var myChart = this.$echarts.init(chartDom);
var option;
var option = {
  tooltip: {
    trigger: 'item',
    formatter:"{a}<br/>{b}: {c}({d}%)"
  },
  toolbox: {
    show: true
  },
  calulable:true,

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
async created(){
    $(document).ready(async()=>{
       
        this.setWorData();
        this.setpieData();
        this.setLastData();     
})
},
  components: {
    LeftTop,
  },
};
</script>

<style lang="less" scoped>
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
.cents {
  display: flex;
  flex-direction: column;
}
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
.cent {
  width: 850px;
  height: 300px;
}

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

.left-1 {
  margin: 15px;
  color: aliceblue;
  width: 550px;
  display: flex;
  flex-direction: column;
}
.left-2 {
  margin: 15px;
  color: aliceblue;
  width: 530px;
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
  margin-top: -20px;
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
  -ms-grid-columns: 30px 110px 60px 60px 60px;
  grid-template-columns: 30px 110px 60px 60px 60px;
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
