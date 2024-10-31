from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import RegistrationForm, OrderProductForm
from .models import User, Order, OrderProduct, Customer


class ManagerRequiredMixin(LoginRequiredMixin):
    """_Check if the user is a manager before granting access to the view_
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.user_type != 1:
            return self.handle_no_permission()
        return super(ManagerRequiredMixin, self).dispatch(request, *args, **kwargs)


class RegistrationView(ManagerRequiredMixin, CreateView):
    template_name = "authentication/registration.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
    
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super(RegistrationView, self).form_valid(form)


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    login_url = reverse_lazy("login")
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all()
        return context
    
    
class OrderProductCreateView(LoginRequiredMixin, CreateView):
    template_name = "order_product/create.html"
    model = OrderProduct
    # form_class = OrderProductForm
    fields = ['order', 'product', 'quantity']
    
    
    # take order information
    # take product order information
    # create order, then create order product
    
    def post(self, request, *args, **kwargs):
        if request.user.user_type == 1 or request.user.user_type == 3:
            
            customer_email = request.POST.get('customer_email')
            order_status = request.POST.get('order_status')
            payment_status = request.POST.get('payment_status')
            product = request.POST.get('product')
            quantity = request.POST.get('quantity')

            # get the customer
            customer = Customer.objects.get(email=customer_email)
            
            # create order
            order = Order.objects.create(
                order_status=order_status,
                payment_status=payment_status,
                customer=customer
            )
            
            # create order product
            order_product = OrderProduct.objects.create(
                order=order,
                product=product,
                quantity=quantity
            )
            order_product.save()
            
            return super(OrderProductCreateView, self).post(request, *args, **kwargs)
    
    
    
    
    
    
    
# class OrderCreateView(LoginRequiredMixin, CreateView):
#     template_name = "order/create.html"
#     model = Order
#     success_url = reverse_lazy("index")
    
    
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(OrderCreateView, self).form_valid(form)

