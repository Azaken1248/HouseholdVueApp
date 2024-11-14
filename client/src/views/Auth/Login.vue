<template>
  <div class="container mt-5">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input type="text" v-model="username" class="form-control" id="username" required />
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" v-model="password" class="form-control" id="password" required />
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
    <button class="btn btn-link mt-3 back-button" @click="goBack">
      &#x2190; Back
    </button>
  </div>
</template>

<script>
import { ref } from 'vue'; 
import { useRoute, useRouter } from 'vue-router'; 
import axios from 'axios'; // Import axios for API requests

export default {
  name: "UserLogin",
  setup() {
    const route = useRoute();
    const router = useRouter(); 

    const role = route.params.role || 'User'; 

    const username = ref(''); // Change email to username
    const password = ref(''); 

    const handleLogin = async () => {
      try {
        const response = await axios.post('http://localhost:5000/api/login', {
          username: username.value, // Use username instead of email
          password: password.value,
        });
        alert("Login successful!");
        //console.log(response);

        localStorage.setItem('access_token', response.data.access_token);
        localStorage.setItem('id',response.data.data.username)

        let role = response.data.data.role;
        if(role === "Admin"){ 
          router.push({ name: 'Dashboard' });
        }else if(role === "User"){
          router.push({name: "UserDashboard"});
        }else if(role === "Service Professional"){
          router.push({name: "ServiceDashboard"});
        }else{
          router.push({name: "UserDashboard"});
        }
      } catch (error) {
        alert(error.response.data.msg || "Login failed");
      }
    };

    const goBack = () => {
      router.push("/")
    };

    return { role, username, password, handleLogin, goBack };
  }
};
</script>

<style scoped>
label {
    color: #00fec3;
}
h2 {
    color: #00fec3;
}
input {
    background-color: #073642;
    border-color: #00fec3;
    color: #00fec3;
}
input:focus {
    background-color: #073642;
    border-color: #00fec3;
    color: #00fec3;
}
.btn-primary {
    background-color: #073642;
    color: #00fec3; /* Button text color */
    border-color: #00fec3; /* Button border color */
}
.btn-primary:hover {
    background-color: #00fec3; /* Button hover color */
    color: #073642; /* Text color on hover */
}
.back-button {
    background: none; /* No background */
    border: none; /* No border */
    color: #00fec3; /* Text color */
    cursor: pointer; /* Pointer cursor */
    font-size: 16px; /* Font size */
    padding: 0; /* No padding */
}
.back-button:hover {
    color: #00fec3; /* Change color on hover */
}
</style>
