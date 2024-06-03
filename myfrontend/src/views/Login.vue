<style>
	.center {
		width: 1920px;
		height: 1080px;
		background-image: url("../assets/bg02.jpg");
		background-size: 100% 100%;
		background-repeat: no-repeat;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}
 
	h1 {
		font-size: 30px;
		color: rgb(17, 169, 229);
	}
 
	.logon {
		background-color: #fff;
		border-radius: 10px;
		box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
		/* position: relative;
		overflow: hidden; */
		width: 768px;
		max-width: 100%;
		min-height: 480px;
		margin-top: 20px;
		display: flex;
		background: -webkit-linear-gradient(right, #4284db, #29eac4);
	}
 
	.overlaylong {
		border-radius: 10px 0 0 10px;
		width: 50%;
		height: 100%;
		background-color: #fff;
		display: flex;
		align-items: center;
		justify-content: center;
	}
 
	.overlaylongleft {
		border-radius: 0px 10px 10px 0px;
		width: 50%;
		height: 100%;
		background-color: #fff;
		transform: translateX(100%);
		transition: transform 0.6s ease-in-out;
		display: flex;
		align-items: center;
		justify-content: center;
	}
 
	.overlaylongright {
		border-radius: 10px 0 0 10px;
		width: 50%;
		height: 100%;
		background-color: #fff;
		transform: translateX(0%);
		transition: transform 0.6s ease-in-out;
		display: flex;
		align-items: center;
		justify-content: center;
	}
 
	.overlaytitle {
		border-radius: 0px 10px 10px 0px;
		width: 50%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0);
		display: flex;
		align-items: center;
		justify-content: center;
	}
 
 
	.overlaytitleH2 {
		font-size: 30px;
		color: #fff;
		margin-top: 20px;
	}
 
	.overlaytitleP {
		font-size: 20px;
		color: #fff;
		margin-top: 20px;
	}
 
	.overlaytitleleft {
		border-radius: 0px 10px 10px 0px;
		width: 50%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0);
		display: flex;
		align-items: center;
		justify-content: center;
		transform: translateX(0%);
		transition: transform 0.6s ease-in-out;
	}
 
	.overlaytitleright {
		border-radius: 0px 10px 10px 0px;
		width: 50%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0);
		display: flex;
		align-items: center;
		justify-content: center;
		transform: translateX(-100%);
		transition: transform 0.6s ease-in-out;
	}
 
	.overlaytitle-Signin {
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}
 
	.overlaytitle-Signup {
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}
 
	.buttongohs {
		width: 180px;
		height: 40px;
		border-radius: 50px;
		border: 1px solid #fff;
		color: #fff;
		font-size: 15px;
		text-align: center;
		line-height: 40px;
		margin-top: 40px;
	}
 
	.overlaylongH2 {
		font-size: 25px;
		color: black;
		/* width: 250px; */
	}
 
	.overlaylong-Signin {
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}
 
	.overlaylong-Signup {
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}
 
	.input {
		background-color: #eee;
		border: none;
		padding: 12px 15px;
		margin: 10px 0;
		width: 240px;
	}
	h3{
		font-size: 10px;
		margin-top: 10px;
		cursor: pointer;
	}
	.inputbutton{
		background-color: #29eac4;
		border: none;
		width: 180px;
		height: 40px;
		border-radius: 50px;
		font-size: 15px;
		color: #fff;	
		text-align: center;
		line-height: 40px;
		margin-top: 30px;
	}
</style>
 
<template>
	<div class="center">
		<div class="logon">
			<div class="overlaylongright">
				<!-- <div class="overlaylong-Signin">
					<h2 class="overlaylongH2">Sign in</h2>
					<input type="text" placeholder="Username" v-model="loginForm.username">
					<input type="password" placeholder="Password" v-model="loginForm.password">
					<h3>Forgot your password?</h3>
					<button class="inputbutton" @click="login">Sign in</button>
				</div> -->
				<div class="overlaylong-Signin">
					<!-- <el-container> -->
					<el-main>
						<div id="login-from">
							<el-form ref="loginForm" status-icon :model="loginForm" :rules="rules">
								<el-form-item label="Username" prop="username">
									<el-input v-model="loginForm.username" autocomplete="off" style="width: 250px;"></el-input>
								</el-form-item>
								<el-form-item label="Password" prop="password">
									<el-input type="password" v-model="loginForm.password" autocomplete="off" style="width: 250px;"></el-input>
								</el-form-item>
								<slide-verification @check-result="checkResult"></slide-verification>
								<br />
								<div style="display: flex; justify-content: center;">
									<el-button class="inputbutton" @click.native.prevent="login('loginForm')">登录</el-button>
								</div>
							</el-form>
						</div>
					</el-main>
					<!-- </el-container> -->
				</div>
			</div>
			<div class="overlaytitleleft">
				<div class="overlaytitle-Signin">
					<h2 class="overlaytitleH2">海洋牧场监测可视化系统</h2>
					<p class="overlaytitleP">
						Still don't have an account?
					</p>
					<router-link class="buttongohs" to="/register">Sign up</router-link>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import SlideVerification from '@/components/SlideVerification.vue'
export default {
	data() {
		return {
			// overlaylong: 'overlaylong',
			// overlaytitle: 'overlaytitle',
			// disfiex: 0,
			confirmSuccess: false,
			loginForm: {
				username: null,
				password: null,
			},
			rules: {
				username: [{
					required: true,
					message: 'Please enter your username',
					trigger: 'blur'
				}],
				password: [{
					required: true,
					message: 'Please enter your password',
					trigger: 'blur'
				}]
			},
		}
	},
	components:{
		SlideVerification
	},
	methods: {
		//获取滑块验证结果
		checkResult(message) {
			this.confirmSuccess = message
		},
		login(formName) {
			//清理缓存信息
			localStorage.clear()
			sessionStorage.clear()
			if (this.confirmSuccess) {
				const msg = this
				this.$refs[formName].validate((valide) => {
					if (valide) {
						axios.post(`myApp/login/`, this.loginForm).then(res => {
							console.log(res); //处理成功的函数 相当于success
							if (res.status == 200) {
								this.$message({
									message: '登录成功',
									type: 'success'
								});
								// console.log(res.data.user)
								// this.$store.commit("setUser", res.body)
								console.log(res.data.fiserman)
								// console.log(res.data.token)
								// this.$store.commit("setAuthorization", res.token)
								this.$store.commit("setUser", res.data.user)
								this.$store.commit("setFisherman", res.data.user)
								this.$store.commit("setAuthorization", res.data.token)
								this.$store.commit('setLogin', true);
								this.$router.push('/')
							}
						}).catch(function(error) {
							//错误处理 相当于error
							msg.$message('登录失败，账号或密码错误');
							console.log(error) 
						});
					} else {
						//表单验证失败
						this.$message('请填写完整信息！');
					}
				});
			} else {
				//未通过验证
				this.$message('请拖动滑块进行验证！');
			}
		}
	}
}
</script>
