<template>
  <div class="container mt-5">
    <h2>Manage Services</h2>
    <form>
      <div class="mb-3">
        <label for="serviceName" class="form-label">Service Name</label>
        <input type="text" class="form-control" id="serviceName" required />
      </div>
      <div class="mb-3">
        <label for="servicePrice" class="form-label">Base Price</label>
        <input type="number" class="form-control" id="servicePrice" required />
      </div>
      <button type="submit" class="btn btn-primary">Add Service</button>
    </form>
    <h3 class="mt-4">Existing Services</h3>
    <ul class="list-group">
      <li v-for="service in services" :key="service.id" class="list-group-item d-flex justify-content-between">
        {{ service.name }} - ${{ service.price }}
        <button class="btn btn-danger btn-sm">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "ManageServices",
  data() {
    return {
      services: [
        { id: 1, name: "Plumbing", price: 100 },
        { id: 2, name: "Electrical Repair", price: 150 },
      ],
    };
  },
};
</script>
