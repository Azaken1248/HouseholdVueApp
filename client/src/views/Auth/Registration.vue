<template>
  <div class="container mt-2">
    <h2>Register as {{ role }}</h2>
    <form @submit.prevent="handleRegistration">
      <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input type="text" v-model="username" class="form-control" id="username" required />
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" v-model="email" class="form-control" id="email" required />
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" v-model="password" class="form-control" id="password" required />
      </div>
      <div class="mb-3">
        <label for="confirm-password" class="form-label">Confirm Password</label>
        <input type="password" v-model="confirmPassword" class="form-control" id="confirm-password" required />
      </div>
      <div class="mb-3">
        <label for="phone" class="form-label">Phone Number</label>
        <input type="tel" v-model="phone" class="form-control" id="phone" required />
      </div>
      <button type="submit" class="btn btn-primary">Register</button>
    </form>
    <button class="btn btn-link mt-3 back-button" @click="goBack">
      &#x2190; Back
    </button>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios'; // Import axios

export default {
  name: "UserRegistration",
  setup() {
    const route = useRoute();
    const router = useRouter();

    const role = route.params.role || 'User'; 
    
    // Reactive properties for registration form
    const username = ref('');
    const email = ref('');
    const password = ref('');
    const confirmPassword = ref('');
    const phone = ref('');

    const handleRegistration = async () => {
      if (password.value !== confirmPassword.value) {
        alert("Passwords do not match!");
        return;
      }

      try {
        const response = await axios.post('https://skibidi2.rrex.cc/api/register', {
          username: username.value,
          password: password.value,
          role: role,
          email: email.value,
          phone: phone.value,
        });
        alert(response.data.msg);
        router.push('/login'); // Redirect to login after successful registration
      } catch (error) {
        alert(error.response?.data.msg || "An error occurred during registration.");
      }
    };

    const goBack = () => {
      router.push("/")
    };

    return { role, username, email, password, confirmPassword, phone, handleRegistration, goBack };
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
