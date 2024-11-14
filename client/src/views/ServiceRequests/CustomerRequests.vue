<template>
  <div class="container mt-5">
    <h3>Request Another Service</h3>
    <form @submit.prevent="submitCustomRequest">
      <div class="form-group mb-3">
        <label for="customServiceType">Service Type</label>
        <input type="text" v-model="customService.type" id="customServiceType" class="form-control" placeholder="Enter service type" required />
      </div>
      <div class="form-group mb-3">
        <label for="customServiceDate">Required Date</label>
        <input type="date" v-model="customService.date" id="customServiceDate" class="form-control" required />
      </div>
      <div class="form-group mb-3">
        <label for="customServiceTime">Required Time</label>
        <input type="time" v-model="customService.time" id="customServiceTime" class="form-control" required />
      </div>
      <div class="form-group mb-3">
        <label for="customServiceAmount">Amount</label>
        <input type="number" v-model="customService.amount" id="customServiceAmount" class="form-control" placeholder="Enter amount" required />
      </div>
      <button class="btn btn-success" type="submit">Submit Request</button>
      <button class="btn btn-secondary" type="button" @click="goBack">Back</button> <!-- Change to 'type="button"' -->
    </form>
  </div>
</template>


<script>
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router'; 

export default {
  name: "ServiceRequestForm",
  setup() {
    const customService = ref({ type: "", date: "", time: "", amount: "" });
    const router = useRouter();

    const submitCustomRequest = async () => {
      try {
        const token = localStorage.getItem('access_token');
        await axios.post('http://localhost:5000/api/service-requests', {
          user_id: localStorage.getItem('id'),
          service_id: Date.now(),
          type: customService.value.type,
          date: customService.value.date,
          time: customService.value.time,
          amount: customService.value.amount,
        }, {
          headers: { Authorization: `Bearer ${token}` }
        });
        alert("Custom service request submitted successfully");
        customService.value = { type: "", date: "", time: "", amount: "" };
      } catch (error) {
        console.error("Error submitting custom service request:", error);
      }
    };

    const goBack = () => {
      router.push("/user/dashboard");
    };

    return { customService, submitCustomRequest, goBack };
  }
};
</script>

<style scoped>
  .form-group label {
    color: #00fec3;
  }
  .form-group input {
    background-color: #073642;
    color: #00fec3;
    border: 1px solid #00fec3;
  }
  button {
    margin-top: 10px;
    margin-left: 10px;
    background-color: #073642;
    color: #00fec3;
    border-color: #00fec3;
  }
  button:hover {
    background-color: #00fec3; 
    color: #073642; 
  }
</style>
