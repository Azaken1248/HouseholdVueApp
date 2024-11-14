<template>
    <div class="container mt-5" v-if="isAuthenticated">
      <h2>Service Professional Dashboard</h2>
  
      <!-- Available Service Requests Section -->
      <div class="row">
        <div class="col-md-12">
          <h3>Available Service Requests</h3>
          <table class="table">
            <thead>
              <tr>
                <th>Request ID</th>
                <th>Service</th>
                <th>Customer</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-if="availableServiceRequests.length === 0">
                <td colspan="4">No available service requests</td>
              </tr>
              <tr v-else v-for="request in availableServiceRequests" :key="request.id">
                <td>{{ request.service_id }}</td>
                <td>{{ request.service }}</td>
                <td>{{ request.user_id }}</td>
                <td>
                  <button class="btn btn-success btn-sm" @click="acceptRequest(request.id)">Accept</button>
                  <button class="btn btn-danger btn-sm" @click="denyRequest(request.id)">Deny</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="row mt-4">
        <div class="col-md-12">
          <h3>Your Accepted Service Requests</h3>
          <table class="table">
            <thead>
              <tr>
                <th>Request ID</th>
                <th>Service</th>
                <th>Customer</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr v-if="userAcceptedDeniedRequests.length === 0">
                <td colspan="4">No accepted or denied service requests</td>
              </tr>
              <tr v-else v-for="request in userAcceptedDeniedRequests" :key="request.id">
                <td>{{ request.service_id }}</td>
                <td>{{ request.service }}</td>
                <td>{{ request.user_id }}</td>
                <td>{{ request.status }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
  
      <!-- Buttons Section -->
      <div class="mt-4">
        <button class="btn btn-primary" @click="logoutUser">Logout</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  
  export default {
    name: "ServiceProfessionalDashboard",
    setup() {
      const availableServiceRequests = ref([]);
      const userAcceptedDeniedRequests = ref([]);
      const isAuthenticated = ref(false);
      const router = useRouter();
  
      // Fetch available service requests from backend
      const fetchAvailableServiceRequests = async () => {
        try {
          const token = localStorage.getItem('access_token');
          const response = await axios.get('http://localhost:5000/api/service-requests/professional', {
            headers: { Authorization: `Bearer ${token}` }
          });
          availableServiceRequests.value = response.data;
        } catch (error) {
          console.error("Error fetching available service requests:", error);
        }
      };
  
      // Fetch accepted or denied requests for the service professional
      const fetchUserAcceptedDeniedRequests = async () => {
        try {
          const token = localStorage.getItem('access_token');
          const response = await axios.get('http://localhost:5000/api/service-requests/professional/approved', {
            headers: { Authorization: `Bearer ${token}` }
          });
          userAcceptedDeniedRequests.value = response.data;
        } catch (error) {
          console.error("Error fetching user accepted or denied requests:", error);
        }
      };
  
      // Accept a service request and update the status locally
      const acceptRequest = async (requestId) => {
        try {
          const token = localStorage.getItem('access_token');
          await axios.patch(`http://localhost:5000/api/service-requests/${requestId}/approve`, {}, {
            headers: { Authorization: `Bearer ${token}` }
          });
  
          // Update local data
          const request = availableServiceRequests.value.find(r => r.id === requestId);
          if (request) {
            request.status = "accepted";
            window.location.reload();
          }
        } catch (error) {
          console.error("Error accepting service request:", error);
        }
      };
  
      // Deny a service request and update the status locally
      const denyRequest = async (requestId) => {
        try {
          const token = localStorage.getItem('access_token');
          await axios.patch(`http://localhost:5000/api/service-requests/${requestId}/deny`, {}, {
            headers: { Authorization: `Bearer ${token}` }
          });
  
          // Update local data
          const request = availableServiceRequests.value.find(r => r.id === requestId);
          if (request) {
            request.status = "denied";
            window.location.reload();
          }
        } catch (error) {
          console.error("Error denying service request:", error);
        }
      };
  
      // Logout user
      const logoutUser = () => {
        localStorage.removeItem("access_token");
        isAuthenticated.value = false;
        router.push({ name: 'Login' });
      };
  
      onMounted(() => {
        const token = localStorage.getItem('access_token');
        if (token) {
          isAuthenticated.value = true;
          fetchAvailableServiceRequests();
          fetchUserAcceptedDeniedRequests();
        } else {
          router.push({ name: 'Login' });
        }
      });
  
      return { 
        availableServiceRequests, 
        userAcceptedDeniedRequests, 
        isAuthenticated, 
        acceptRequest, 
        denyRequest, 
        logoutUser 
      };
    }
  };
  </script>
  
  <style scoped>
  table th {
    background-color: #073642;
    border: 1px solid #00fec3;
    color: #00fec3;
  }
  table tr td {
    background-color: #073642;
    border: 1px solid #00fec3;
    color: #00fec3;
  }
  button {
    margin: 10px;
    background-color: #073642;
    color: #00fec3;
    border-color: #00fec3;
  }
  button:hover {
    background-color: #00fec3;
    color: #073642;
  }
  </style>
  