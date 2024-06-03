<style>
	.center {
		width: 1920px;
		height: 1080px;
		background-image: url("../assets/oceanBg.png");
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
 
	input {
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
	.inupbutton{
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
	
	.text-foot{
		font-weight: 700;
		margin-top: 20px;
		display: flex;
		justify-content: center;
	}
</style>
 
<template>
    <div class="center">
		<div class="logon">
            <div :class="overlaylong">
				<div class="overlaylong-Signin" v-if="disfiex == 0">
					<el-main>
						<div id="register-from">
							<el-form ref="registerForm" status-icon :model="registerForm" :rules="rules">
								<el-form-item label="Username" prop="username" style="margin-bottom: 5px;">
									<el-input v-model="registerForm.username" autocomplete="off" style="width: 250px;"></el-input>
								</el-form-item>
								<el-form-item label="Name" prop="name" style="margin-bottom: 5px;">
									<el-input v-model="registerForm.name" autocomplete="off" style="width: 250px;"></el-input>
								</el-form-item>
								<el-form-item label="Phone" prop="phone" style="margin-bottom: 5px;">
									<el-input v-model="registerForm.phone" autocomplete="off" style="width: 250px;"></el-input>
								</el-form-item>
								<div class="text-foot">
									已有账号？
									<router-link to="/login" class="register-link">
										登录
									</router-link>
								</div>
							</el-form>
						</div>
					</el-main>
				</div>
				<div class="overlaylong-Signup" v-if="disfiex == 1">
					<el-main>
						<div id="register-from">
							<el-form ref="registerForm" status-icon :model="registerForm" :rules="rules">
								<el-form-item label="E-mail" prop="email" style="margin-bottom: 5px;">
									<el-input v-model="registerForm.email" autocomplete="off" style="width: 250px;"></el-input>
								</el-form-item>
								<el-form-item label="Password" prop="password" style="margin-bottom: 5px;">
									<el-input type="password" v-model="registerForm.password" autocomplete="off" style="width: 250px;"></el-input>
								</el-form-item>
								<el-form-item label="Confirm Your Passord" prop="checkpwd" style="margin-bottom: 5px;">
									<el-input type="password" v-model="registerForm.checkpwd" autocomplete="off" style="width: 250px;"></el-input>
								</el-form-item>
								<slide-verification @check-result="checkResult"></slide-verification>
								<br />
								<div style="display: flex; justify-content: center;">
									<el-button class="inputbutton" @click.native.prevent="register('registerForm')">注册</el-button>
								</div>
							</el-form>
						</div>
					</el-main>
				</div>
			</div>
            <div :class="overlaytitle">
				<div class="overlaytitle-Signin" v-if="disfiex == 0">
					<h2 class="overlaytitleH2">海洋牧场监测可视化系统</h2>
					<p class="overlaytitleP">Next step is to create an account</p>
                    <div class="buttongohs" @click="NextStep">Next Step</div>
				</div>
				<div class="overlaytitle-Signin" v-if="disfiex == 1">
					<h2 class="overlaytitleH2">海洋牧场监测可视化系统</h2>
					<p class="overlaytitleP">The last step is to create an account</p>
                    <div class="buttongohs" @click="LastStep">Last Step</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import SlideVerification from '@/components/SlideVerification.vue'
export default {
    data() {
        var validatePass = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请输入密码'));
            } else {
                if (this.registerForm.checkpwd !== '') {
                    this.$refs.registerForm.validateField('checkpwd');
                }
                callback();
            }
        };
        var validatePass2 = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('请再次输入密码'));
            } else if (value !== this.registerForm.password) {
                callback(new Error('两次输入密码不一致!'));
            } else {
                callback();
            }
        };
        return {
            confirmSuccess: false,
			overlaylong: 'overlaylong',
			overlaytitle: 'overlaytitle',
			disfiex: 0,
            registerForm: {
                username: null,
                password: null,
                checkpwd: null,
                name: null,
				phone: null,
				email: null
            },
            rules: {
                username: [{
                        required: true,
                        message: '请输入用户名',
                        trigger: 'blur'
                    },
                    {
                        min: 6,
                        max: 15,
                        message: '长度在 6 到 15 个字符',
                        trigger: 'blur'
                    }
                ],
                password: [{
                        required: true,
                        message: '请输入密码',
                        trigger: 'blur'
                    },
                    {
                        min: 6,
                        max: 10,
                        message: '长度在 6 到 15 个字符',
                        trigger: 'blur'
                    },
                    {
                        validator: validatePass,
                        trigger: 'blur'
                    }
                ],
                checkpwd: [{
                        required: true,
                        message: '请再次输入密码',
                        trigger: 'blur'
                    },
                    {
                        min: 6,
                        max: 15,
                        message: '长度在 6 到 10 个字符',
                        trigger: 'blur'
                    },
                    {
                        validator: validatePass2,
                        trigger: 'blur'
                    }
                ],
                name: [{
                        required: true,
                        message: 'Please enter your name',
                        trigger: 'blur'
                    },
                    {
                        min: 2,
                        max: 10,
                        message: '长度在 2 到 8 个字符',
                        trigger: 'blur'
                    }
                ],
				phone: [{
						required: true,
						message: 'Please enter your phone number',
						trigger: 'blur'
					},
					{
						pattern: /^1[3|4|5|6|7|8|9][0-9]\d{8}$/,
						message: '长度为11个字符',
						trigger: ['blur', 'change']
					}
				],
				email: [{
						required: true,
						message: 'Please enter your email',
						trigger: 'blur'
					},
					{
						type: 'email',
						message: 'Please enter the correct email address',
						trigger: 'blur'
					}
				]
            }
        }
    },
    components: {
        SlideVerification
    },
    methods: {
		NextStep() {
				this.overlaylong = "overlaylongleft"
				this.overlaytitle = "overlaytitleright"
				setTimeout(() => {
					this.disfiex = 1
				}, 200)
			},
		LastStep() {
			this.overlaylong = "overlaylongright"
			this.overlaytitle = "overlaytitleleft"
			setTimeout(() => {
				this.disfiex = 0
			}, 200)
		},
        //获取滑块验证结果
        checkResult(message) {
            this.confirmSuccess = message
        },
        //处理注册
        register(formName) {
            if (this.confirmSuccess) {
                const msg = this
                this.$refs[formName].validate((valide) => {
                    if (valide) {
                        axios.post(`myApp/register/`, this.registerForm).then(res => {
                            console.log(res); //处理成功的函数 相当于success
                            if (res.status == 200) {
                                this.$message({
                                    message: '注册成功',
                                    type: 'success'
                                });
                                this.$router.push('/login')
                            } else {
                                this.$message({
                                    message: res.data.msg,
                                    type: 'error'
                                });
                            }
                        }).catch(function(error) {
                            msg.$message('注册失败');
                            console.log(error) //错误处理 相当于error
                        });
                    } else {
                        //表单验证失败
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